# This API for Questioner AI,

## this api ask user these info
### full_name:Optional[str]   = Field(default="",description="full name of user") 
###     age: Optional[str] = Field(default="",description="age of user") 
###     nationality:Optional[str]  = Field(default="",description="user nationality ")
###     savings:Optional[str]   = Field(default="",description="total savings of user")
###     yearly_salary:Optional[str]  = Field(default="",description="yearly salary of user")
###     education:Optional[str]  = Field(default="",description="education degree/level of user")
###     language_proficiency_score:Optional[str]  = Field(default="",description="ilets or toefl or any other language test ### score")
###     immigration_plan:Optional[str]  = Field(default="no immigration plan",description="immigration plan of user")
###     work_experience:Optional[str]  = Field(default="",description="total years of user experience and field")
###     maritial_status:Optional[str]  = Field(default="",description="single or married")
###     number_of_kids:Optional[str]  = Field(default="",description="how many kids user has")
###     preferred_countries : Optional[list[str]]   = Field(default=["No preferred country"],description="list of countries ### user preferred to go,")




## Method
post
## url
'/invoke/questioner'


## Response Format
output = {
            "ai_response" : result['structured_response'].ai_response,
            "structure_output" : result['structured_response']
        }