def teacherCheck(value ,items,new_key):
    for idx, item in enumerate(value):
        for k, v in item.items():
            items.append((f"{new_key}_{idx}_{k}", v))
    return items

def flateDic(Json, parent_key='', sep='_'):
    items = []
    for key, value in Json.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flateDic(value, new_key, sep=sep).items())
        elif isinstance(value, list):
            teacherCheck(value,items,new_key)
        else:
            items.append((new_key, value))
    return dict(items)

Json = {
    "_id": "6575606b68a8775e01f1bed2",
    "lessonPlanId": "6574856f68a8775e01efcfd5",
    "classId": "6564a76624f91124a53ca96f",
    "className": "12",
    "subject": "Mathematics",
    "topic": "APPLICATIONS OF DERIVATIVES",
    "section": "PCM B",
    "status": "Achieved",
    "statusUpdateTime": "2023-05-12 09:54:28",
    "createdDate": "2023-05-12",
    "hwProcessId": "79892_school_process1",
    "hwAssignment": "yes",
    "hwAssignmentStatus": "Achieved",
    "hwAssignmentId": "",
    "academicYear": "2023-24",
    "version": "2",
    "homeworkAssignment": {
        "allocation": {
            "assignByDate": "12/05/2023",
            "assignmentGivenDate": "12/05/2023",
            "submissionDate": "16/05/2023",
            "filePath": ""
        },
        "collection": {
            "history": [
                {
                    "collectionDate": "18/05/2023",
                    "submissionStatus": "all",
                    "remarks": "",
                    "collectionStatus": "completed"
                }
            ],
            "overallSubmissionStatus": "yes"
        },
        "evaluation": {
            "remarks": "",
            "date": "18/05/2023"
        }
    },
    "teachers": [
        {
            "teacherId": "6568860d0e0d0559d76dfcc5",
            "teacherName": "Keshav Dev Sharma"
        },
        {
            "teacherId": "6568860d0e0d0559d76dfcc5",
            "teacherName": "Keshav Dev Sharma"
        }
    ],
    "_class": "com.xtremesoftech.eims.lessonoutcometracker.model.LessonOutcomeTracker"
}

flateJson = flateDic(Json)

print("{")
for key, value in flateJson.items():
    print(f'    "{key}": "{value}",')
print("}")