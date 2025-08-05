import requests
import json



#Load enterprise attack file or download the data
try:
    with open("enterprise-attack.json", "r") as file:
        mitre_data = file.read()
        mitre_data = json.loads(mitre_data)
except FileNotFoundError:
    mitre_file = requests.get("https://raw.githubusercontent.com/mitre/cti/refs/heads/master/enterprise-attack/enterprise-attack.json")
    with open("enterprise-attack.json", "w") as file:
        mitre_data = file.write(mitre_file.text)
    mitre_data = mitre_file.json()


#Create dictionary
matrix = {"tactics": {}}

#Get tactics and associated information
for object in mitre_data["objects"]:
    if object.get("type") == "x-mitre-tactic":
        tactic_name = object.get("name")
        matrix["tactics"][tactic_name] = {}
        matrix["tactics"][tactic_name]["description"] = object.get("description")
        matrix["tactics"][tactic_name]["shortname"] = object.get("x_mitre_shortname")
        for ref in object.get("external_references"):
            matrix["tactics"][tactic_name]["url"] = ref.get("url")
            matrix["tactics"][tactic_name]["id"] = ref.get("external_id")
        matrix["tactics"][tactic_name]["techniques"] = {}

#Get techniques and associated information
for object in mitre_data["objects"]:           
    if object.get("type") == "attack-pattern":
        #print(object.get("name"))
        technique_name = object.get("name")
        is_subtechnique = object.get("x_mitre_is_subtechnique")
        if is_subtechnique is False:
            for key in object.get("kill_chain_phases"):
                phase = key.get("phase_name")
                for tactic in matrix["tactics"]:
                    if phase == matrix["tactics"][tactic]["shortname"]:
                        matrix["tactics"][tactic]["techniques"][technique_name] = {}
                        #matrix["tactics"][tactic]["techniques"][technique_name]["is_subtechnique"] = object.get("x_mitre_is_subtechnique")
                        matrix["tactics"][tactic]["techniques"][technique_name]["description"] = object.get("description")
                        for ref in object.get("external_references"):
                            if ref.get("source_name") == "mitre-attack":
                                matrix["tactics"][tactic]["techniques"][technique_name]["id"] = ref.get("external_id")
                                matrix["tactics"][tactic]["techniques"][technique_name]["url"] = ref.get("url")
                                matrix["tactics"][tactic]["techniques"][technique_name]["subtechniques"] = {}
                                

#Get subtechniques and associated information
for object in mitre_data["objects"]:           
    if object.get("type") == "attack-pattern":
        subtechnique_name = object.get("name")
        is_subtechnique = object.get("x_mitre_is_subtechnique")
        if is_subtechnique is True:
            for ref in object.get("external_references"):
                if ref.get("source_name") == "mitre-attack":
                    sub_id = ref.get("external_id")
                    for tactic in matrix["tactics"]:
                        for technique in matrix["tactics"][tactic]["techniques"]:
                            if matrix["tactics"][tactic]["techniques"][technique]["id"] in sub_id:
                                matrix["tactics"][tactic]["techniques"][technique]["subtechniques"][subtechnique_name] = {}
                                #matrix["tactics"][tactic]["techniques"][technique]["subtechniques"][subtechnique_name]["is_subtechnique"] = object.get("x_mitre_is_subtechnique")
                                matrix["tactics"][tactic]["techniques"][technique]["subtechniques"][subtechnique_name]["description"] = object.get("description")
                                for ref in object.get("external_references"):
                                    if ref.get("source_name") == "mitre-attack":
                                        matrix["tactics"][tactic]["techniques"][technique]["subtechniques"][subtechnique_name]["id"] = ref.get("external_id")
                                        matrix["tactics"][tactic]["techniques"][technique]["subtechniques"][subtechnique_name]["url"] = ref.get("url")
                                

#Sort techniques in alphebetical order
for tactic in matrix["tactics"]:
    techniques = matrix["tactics"][tactic]["techniques"]
    sorted_tech = dict(sorted(techniques.items(), key=lambda item: item[0]))
    matrix["tactics"][tactic]["techniques"] = sorted_tech

#Sort subtechniques by id
for tactic in matrix["tactics"]:
    for technique in matrix["tactics"][tactic]["techniques"]:
        subtechniques = matrix["tactics"][tactic]["techniques"][technique]["subtechniques"]
        sorted_subs = dict(sorted(subtechniques.items(), key=lambda item: item[1]["id"]))
        matrix["tactics"][tactic]["techniques"][technique]["subtechniques"] = sorted_subs                                

with open("mitre_simplified.json", 'w') as file:
    json.dump(matrix, file, indent=4)






