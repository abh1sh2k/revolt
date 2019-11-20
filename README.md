#Tasks
1)Sql queries is in file query1.sql and query2.sql

2)Task 1 file is nest.py. We can run this file like : - cat input.json | python nest.py currency country city

3)For task 2 I have used flask . file is app.py
  
  i)To run it simply use python app.py.
  
  ii)To make post request :-
    
    curl -XPOST -H "Content-Type: application/json" localhost:5000/nest/test,test2 --user Us3r:'P@ssw()rd' -d '{"test":"hello"}'