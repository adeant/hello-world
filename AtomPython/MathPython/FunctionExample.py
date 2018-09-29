def build_profile(first='john', last='doe', **user_info):
    """build a dictionary w info about user"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user = build_profile()
print(user)
