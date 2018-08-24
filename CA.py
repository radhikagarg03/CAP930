Employee={"Company:":"TCS",
                      "Branch:":"Banglore",
                        "Department:":"IT",
                        "EmpId:":('10181'),                                                                 #I used employee id as tuple so that no can change it
                      "Positions:":["Project Manager","Software Developer","Data Engineer"],            #i created positions as a list because a person can work in many position in an organizations
                      "Address:":"Delhi",
                        "EmpName:":"Radhika Garg",
                        "DOB:":("03/08/1997"),
                          "Academics:":{"post-graduation:":"MCA","Graduation:":"B.Sc"},
                          "skills:": {"Python","R","Java"},                                                         #i created skills as a set to overcome the witing the skills twice.
                          "Salary:":"20k"
                      }
for k,v in Employee.items():
    print(k,v)
    
    
