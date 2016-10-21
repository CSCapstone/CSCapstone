# CS Capstone Marketplace

## Synopsis

A marketplace for students/groups to find creative and challenging projects to work on. Projects will be provided by industry engineers.  

## Features

- [ ] Common Templating Source (Harris)
- [ ] Authentication Module (Naman)
	- [X] Create (Register) User
		- [ ] Add Form Styling
		- [ ] Seperate Login/Register/Profile Template Files
	- [X] Login
		- [X] Integrate with Django Authentication System
	- [ ] Change Password
	- [ ] Password Reset (sending email)
	- [ ] Student Model using OneToOneField
	- [ ] Teacher Model using OneToOneField
	- [ ] Engineer Model using OneToOneField
- [ ] Project Module (Harris)
	- [X] View Projects List
	- [ ] View Project
	- [ ] Create Project (Name, Description)
- [X] Company Module (Jacob)
- [ ] University Model
- [ ] Class Model (belongs to University)
- [ ] Groups Module
	- [X] Create Groups
	- [X] Add Users to Groups
	- [X] List Groups your in
	- [X] List members in group
	- [ ] Advanced Group Profiles (Strengths, Weaknesses)
- [ ] Student Profile (Major, Year, Skills, Experience Resume, etc)
- [ ] Teacher Profile (Contact Info)
- [ ] Engineer Profile (Alma Mater, About, Contact Info, etc)
- [ ] Inter-Model Associations
	- [ ] Student + Group (Student manytomany Group)
	- [ ] Group + Project (Group manytoone Project)
	- [ ] Student + University (Student belongsTo University)
	- [ ] University + Class (Class belongsTo University)
	- [ ] Engineer + Company (Engineer manytomany Company)

## Contributors

@harrischristiansen (http://www.harrischristiansen.com)  
@thenamanpat  
@dunbarj (http://www.jacobfdunbar.com)
