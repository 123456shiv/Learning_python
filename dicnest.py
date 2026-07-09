team = {
    'emp_01': {
        'name': 'Alice',
        'role': 'Developer',
        'skills': ['Python', 'SQL']
    },
    'emp_02': {
        'name': 'Bob',
        'role': 'Designer',
        'skills': ['Figma', 'CSS']
    }
}

for emp_id, emp_info in team.items():
    print(f"Employee ID: {emp_id}")
    for key, value in emp_info.items():
        print(f"  {key}: {value}")
    print()