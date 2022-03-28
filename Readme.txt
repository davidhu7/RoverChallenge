David Hu

To run this program type "python3 main.py" in the command line in this folders directory

An API design I would create for this application would be to first create the following endpoints:

a GET request with the URL: sitter/:name:/sitter_email which returns the user information(name,email,various scores) in a json object 
The database could use name and email as primary keys and this GET request would try to match the name and email
If the database returns false(no match on name and email combination) then we can return a 404 error otherwise 200 if the database has a match
The name and email are necessary as primary keys as there could be multiple people with same names but the same
name and email combination would be very highly unlikely to have duplicates

a POST request with the URL: sitter/ which allows the user to add a sitter with the necessary information in the request body
If there is a value missing from the header or row then return a 400 error
If the database finds a match with the name and email that is trying to be added then return a 409 error
Otherwise return 201 success 

Then I would expand with the other necessary endpoints such as delete a sitter and update a sitter 

Created the following 3 test cases to test the search_score algorithm:

Test1: A test.csv with a user with a profile score of 2.5 and 5 times of sitting with 5 rating score
According to the readme the correct search score is 3.75 and testres.csv validates this with a 3.75 as the search_score

Test2: A test2.csv with a user with a profile score of 2.5 and 7 times of sitting with 5 rating score
According to the readme the correct search score is 4.25 and test2res.csv validates this with a 4.25 as the search_score

Test3: A test3.csv with a user with a profile score of 2.5 and 11 times of sitting with 5 rating score
According to the readme the correct search score is 5 and testres.csv validates this with a 5 as the search_score

To test these test cases go into main and change the fopen variable to the file that you want to read from and fwrite variable to the file you want to write to