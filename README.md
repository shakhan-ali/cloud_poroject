To run this project please navigate to the folder where the docker-compose is located .
Then rund the following commands:

docker-compose build --no-cache
docker-compose up -d 


plseas wait for a while so all containers are started and then nvavigate to:
http://<external-ip address>:8070/   or http://<localhost-ip address>:8070/
Note: inatilly Nginx my show an error message 502 Bad Gateway, please ignor the message 
and wiat till all containers are ready then refresh the page and it should work.


once the page is loaded please rund the following commands to create an admin:

docker-compose exec web python manage.py createsuperuser

Then provide your username, email and password for the django adminstration

once done please navigate to: http://<external-ip address>/anything-but-admin/
There you would see all the models (relations) plese poulate the ARTICLAE and BOOK model with some test data
then navigate to   http://<external-ip address>:8070/   
 

