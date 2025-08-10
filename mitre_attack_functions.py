import requests
import json
import random


#Load enterprise attack file or download the data
try:
    with open("mitre_simplified.json", "r") as file:
        mitre_data = file.read()
        mitre_data = json.loads(mitre_data)
except FileNotFoundError:
    mitre_file = requests.get("https://raw.githubusercontent.com/garyshear/mitre_attack_simplified/refs/heads/main/mitre_simplified.json")
    with open("mitre_simplified.json", "w") as file:
        mitre_data = file.write(mitre_file.text)
    mitre_data = mitre_file.json()

def get_all_tactics():
    """
    List all tactics

    returns:
    list: lists all tactics
    """
    all_tactics = []
    for tactic in mitre_data["tactics"]:
        all_tactics.append(tactic)
    return all_tactics
        

def get_tactic(tactic):
    """
    Get information on a particular tactic

    input:
    str: tactic name

    returns:
    dict: dictionary with tactic description, id and url
    """
    try:
        tact_dict = {'name': tactic,
                     'description': mitre_data["tactics"][tactic]["description"],
                     'id': mitre_data["tactics"][tactic]["id"],
                     'url': mitre_data["tactics"][tactic]["url"]
                    }
    except:
        return print("Invalid tactic")
        
    return tact_dict
    

def get_techniques_from_tactic(tactic):
    """
    Get a list of techniques from a tactic

    input:
    str: tactic name

    returns:
    list: list of all techniques from a tactic
    """
    techniques = []
    try:
        for technique in mitre_data["tactics"][tactic]["techniques"]:
             techniques.append(technique)
    except:
        print("Not a valid tactic")

    return techniques

def get_technique(technique):
    """
    Get information on a technique

    input:
    str: technique name

    returns:
    dict: dict with technique name, description, id and url
    """
    try:
        for tactic in mitre_data["tactics"]:
            for x in mitre_data["tactics"][tactic]["techniques"]:
                if x == technique:
                    tech_dict = {'name': technique,
                                'description':  mitre_data["tactics"][tactic]["techniques"][technique]["description"],
                                'id': mitre_data["tactics"][tactic]["techniques"][technique]["id"],
                                'url': mitre_data["tactics"][tactic]["techniques"][technique]["url"]
                                }
    except:
        print("Not a valid technique")
    return tech_dict
                
def get_subtechniques_from_technique(technique_name):
    """
    Get a list of subtechniques from a technique

    input:
    Technique name

    returns:
    list: List of subtechniques
    
    """
    subtechniques = []
    try:
          for tactic in mitre_data['tactics']:
             for technique in  mitre_data['tactics'][tactic]['techniques']:
                 if technique == technique_name:
                    for subtech in  mitre_data['tactics'][tactic]['techniques'][technique]['subtechniques']:
                        subtechniques.append(subtech)
    except:
        print("Not a valid technique")
    return subtechniques

    
def get_subtechnique(subtech_name):
    """
    Get information of a specific subtechnique

    input:
    Subechnique name

    returns:
    dict: Dictionary with information on subtechnique
    
    """
    try:
        for tactic in mitre_data["tactics"]:
            for technique in mitre_data["tactics"][tactic]["techniques"]:
                    for subtechnique in mitre_data["tactics"][tactic]["techniques"][technique]['subtechniques']:
                        if subtechnique == subtech_name:
                            subtech_dict = {'name': subtechnique,
                                        'description':  mitre_data["tactics"][tactic]["techniques"][technique]['subtechniques'][subtechnique]["description"],
                                        'id': mitre_data["tactics"][tactic]["techniques"][technique]['subtechniques'][subtechnique]["id"],
                                        'url': mitre_data["tactics"][tactic]["techniques"][technique]['subtechniques'][subtechnique]["url"]
                                        }
    except:
        print("Not a valid subtechnique")

    return subtech_dict


def get_ttp_by_id(id):
    """
    Get information of a specific TTP based on the id
    ex. T1139

    input:
    TTP ID

    returns:
    dict: Dictionary with information on the TTP
    
    """
    try:
        for tactic in mitre_data["tactics"]:
            if id == mitre_data["tactics"][tactic]['id']:
                ttp_dict = {'name': tactic,
                    'description': mitre_data["tactics"][tactic]["description"],
                    'id': mitre_data["tactics"][tactic]["id"],
                    'url': mitre_data["tactics"][tactic]["url"]
                    }
            else:
                for technique in mitre_data["tactics"][tactic]['techniques']:
                    if id ==  mitre_data["tactics"][tactic]['techniques'][technique]['id']:
                        ttp_dict = {'name': technique,
                                    'description':  mitre_data["tactics"][tactic]["techniques"][technique]["description"],
                                    'id': mitre_data["tactics"][tactic]["techniques"][technique]["id"],
                                    'url': mitre_data["tactics"][tactic]["techniques"][technique]["url"]
                                    }
                    else:
                        for subtechnique in mitre_data["tactics"][tactic]['techniques'][technique]['subtechniques']:
                            if id == mitre_data["tactics"][tactic]['techniques'][technique]['subtechniques'][subtechnique]['id']:
                                ttp_dict = {'name': subtechnique,
                                            'description':  mitre_data["tactics"][tactic]["techniques"][technique]['subtechniques'][subtechnique]["description"],
                                            'id': mitre_data["tactics"][tactic]["techniques"][technique]['subtechniques'][subtechnique]["id"],
                                            'url': mitre_data["tactics"][tactic]["techniques"][technique]['subtechniques'][subtechnique]["url"]
                                            }
    except:
        return print("ID not valid")        
    return ttp_dict


def get_ttp_by_name(name):
    """
    Get information of a specific TTP based on the name

    input:
    TTP name

    returns:
    dict: Dictionary with information on the TTP
    
    """
    try:
        for tactic in mitre_data["tactics"]:
            if name == tactic:
                ttp_dict = {'name': tactic,
                    'description': mitre_data["tactics"][tactic]["description"],
                    'id': mitre_data["tactics"][tactic]["id"],
                    'url': mitre_data["tactics"][tactic]["url"]
                    }
            else:
                for technique in mitre_data["tactics"][tactic]['techniques']:
                    if name ==  technique:
                        ttp_dict = {'name': technique,
                                    'description':  mitre_data["tactics"][tactic]["techniques"][technique]["description"],
                                    'id': mitre_data["tactics"][tactic]["techniques"][technique]["id"],
                                    'url': mitre_data["tactics"][tactic]["techniques"][technique]["url"]
                                    }
                    else:
                        for subtechnique in mitre_data["tactics"][tactic]['techniques'][technique]['subtechniques']:
                            if name == subtechnique:
                                ttp_dict = {'name': subtechnique,
                                            'description':  mitre_data["tactics"][tactic]["techniques"][technique]['subtechniques'][subtechnique]["description"],
                                            'id': mitre_data["tactics"][tactic]["techniques"][technique]['subtechniques'][subtechnique]["id"],
                                            'url': mitre_data["tactics"][tactic]["techniques"][technique]['subtechniques'][subtechnique]["url"]
                                            }
    except:
        return print("TTP name not valid")
    return ttp_dict

def get_random_ttp():
    """
    Get information on a random TTP

    returns:
    dict: Dictionary with information on the random TTP
    
    """    
    name_list = []
    for tactic in get_all_tactics():
        name_list.append(tactic)
        for technique in get_techniques_from_tactic(tactic):
            name_list.append(technique)
            for subtechnique in get_subtechniques_from_technique(technique):
                name_list.append(subtechnique)
    return print(get_ttp_by_name(random.choice(name_list)))          
                
