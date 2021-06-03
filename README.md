 # Learning Management System

Install the requirements: `pip install -r requirements.txt`

## Entities

1. Program
2. Student
3. Semester
4. Course
5. Instructor

## Routes For CRUD

| Routes | Method | Description |
| ------ | ------ | -------             | 
|` '/program'` | GET/POST | fetching/posting program data  |
|` '/program/<int:p_id>'` | GET/DELETE/PUT | fetching/deleting/updating program data by id     |
| `'/semester'`  |    GET/POST |  fetching/posting semester data |
| `'/semester/<int:sem_id>'`  | GET/DELETE/PUT  |fetching/deleting/updating semester data by id|
| `'/instructor' ` | GET/POST  | fetching/posting instructor data|
| `'/instructor/<int:ins_id>'`  | GET/DELETE/PUT  |fetching/deleting/updating instructor data by id |
| `'/course'`  |   GET/POST| fetching/posting course data|
| `'/course/<int:c_id>'`  |  GET/DELETE/PUT |fetching/deleting/updating course data by id|
| `'/student'`  |  GET/POST | fetching/posting student data|
| `'/student/<int:s_id>'`  |GET/DELETE/PUT  | fetching/deleting/updating student data by id|


## Routes for Queries

| Routes | Description|
| ------ | ------ |
| `'/sc'`| Total student Count |
| `'/StdSem/<string:prg_name>'` |Number of Student in each Semester by Program |
| `'/CourseFind/<string:prg_name>'`  |Finding Course By Program|
|`'/SecCBSem/<string:prg_name>'`| Section in Each Semester|
|`'/StdCBPrg'`|Student Count By Program|
|`'/InsList/<string:prg_name>'`|Instructor List in Each Semester By Program|
|`'/stdCBSec/<string:prg_name>'`|Student Count in each Section by Program |



Run the Flask Server using  `flask run`
