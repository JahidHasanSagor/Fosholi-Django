# Project created with Django for well distrubution of grown rice across the country so that every farmer can get a fair price for their paddy.
# Idea selected in first round of ICT Innovation Fund 2019, ICT Division, Bangladesh

# Fosholi-Python


Software Requirement
Specification

Fosholi  for Farmers 
Prepared By:
Jahid Hasan Sagor(171-35-1991)
Md. Aftabul Hoque(171-35-1989)
Ajijul Hakim Abid(171-35-1987)

Section: C




Daffodil International University

16th October, 2019


1.	Introduction

1.1	Case Study
The government has been making good progress in buying rice from millers but it is lagging far behind its target for buying paddy from farmers, who had protested recently for not getting decent price for their produce. 
With only a month and week left until the government procurement ends, the food ministry has only been able to buy, as of July 15, less than 30 percent of its paddy purchase target of 4 lakh tons. In stark contrast is the government’s progress in buying rice from millers. Since the procurement began on April 25, it has bought 69 percent of its target of 11.5 lakh tons.

1.2	Finding the gap
 	The Government are lagging behind its target of buying paddy from growers.
 	The Government is unlikely to achieve its buying targets before the deadline.
 	The growers are not able to sell paddy at the price that Govt. fixed.
 	The millers are being benefited not the growers.
 	Farmers can’t sell paddy because they didn’t get enlisted.

1.3	 Motivation
The motivation of this system we got from the incident that farmer burned their own paddy. It is painful to hear that because rice is our main food. We mainly live on rice. One farmer said that a kg of paddy was being sold for Tk 16 to millers where Govt. buys from farmer at Tk 26. 
Farmer Milon Islam said, “I cultivated paddy on 25 bighas of land but could not sell a single kg to the government as I could not get enlisted.” That is why we want to develop this system.



1.4	Goal
The goal of this project is to reach to the paddy growers and buy paddy from them. On the contrary, reaching Govt. paddy buying target directly from farmer. Helping our farmers and make benefited them.



1.5	Stakeholder
The stakeholders are in this system are: 
 	Farmers
 	Govt.
 	Whole population of Bangladesh
 	Retailers


1.6	 Feasibility Study

1.	Technical feasibility 
The project “Fosholi” is a web based software. It’ll be built using Django (python framework) on server side and HTML, CSS, JavaScript on the frontend. All these tools are free to use. These are widely used web technologies and has a large user community. These technologies has maximum compatibility support and are easy to deploy in the server. The can be accessed by any smart device having an internet connection. 
The developers behind the project have required technical skills to implement this project in the given schedule. So this project is technologically feasible.

2.	Economic Feasibility
This project “Fosholi” can be built using the current computers in the organization and the tools used in this project are free to use. So no budget will be required to buy new devices. Some budget is required to do field study to get a better understanding of current agricultural system. This system can be economically beneficial to both farmers and government

3.	Operational Feasibility
This project will introduce Information Technology in our agricultural system. Our current agricultural system has many flaws and many time farmers don’t even make up for their investment by selling crops. After implementing this project will create a connection between farmers and government and both will benefit from the system. Farmers will get a proper price for their crops and government will be able to track various agricultural information like a prediction of how much crops might be produced from a specific area.

4.	Social Feasibility
Our farmers are not very familiar with using this kind of technology. So they have to be educated first about the benefits of using this system. That’s A trained government official will collect data from farmers until farmers can use the system themselves.



1.7	Budget Estimation

Type	Items	Units/hrs	Cost per unit/
Cost per hrs	Subtotal	Level Total
Project Management	Project Manager	200 hrs	80 $	16000$	34000$
	Developer 1	100 hrs	 50 $	5000 $	
	Developer 2	100 hrs	 50 $	5000 $	
	Developer 3	100 hrs	40 $ 	4000 $	
	Tester	50 hrs	40 $	4000 $	
Hardware	Servers	1	5000$	5000 $	9500$
	Computer	5	700$	3500 $	
	Smartphone	5	200$	1000 $	
Software	Domain	1	100$	 100$	1100$
	Licensed software	10	100$	1000 $	
Training & Manpower	Trainee cost	200 hrs	20$	 4000 $	4000$
	Travel cost			1000 $	
				Total budget	49000$


2.	Requirement Analysis

2.1	Functional Requirement

2.1.1 Farmer
FR-01	Login and Logout 
Description 	User will be able to login and logout to the system with valid user credentials.
Stakeholders 	Farmer
Priority 	High 

FR-02	Check Notice Board 
Description 	Farmer can able to check notice board about Govt. provided fertilizer , pesticide , date of buying paddy etc.
Stakeholders 	Farmer, Krishi Officer
Priority 	Medium 

FR-03	Upload details about estimated paddy
Description 	In order to get enlisted by Union Agriculture Office, Farmer need to upload details about their cultivated land and estimated paddy.
Stakeholders 	Farmer, Krishi Officer
Priority 	High 

FR-04	Ask query
Description 	Farmer can ask any query about  cultivation
Stakeholders 	Farmer, Krishi Officer
Priority 	Medium

FR-05	Sell crops to retailer 
Description 	Farmer can sell crops like vegetables to retail market directly through this system.
Stakeholders 	Farmer, Retailer 
Priority 	Medium
    
2.1.2 Krishi Officer
FR-01	Login and Logout 
Description 	User will be able to login and logout to the system with valid user credentials.
Stakeholders 	Farmer
Priority 	High 

FR-02	Validate farmer application 
Description 	Krishi Officer need to check and approve farmer application for making a list from whom Govt. will buy paddy.
Stakeholders 	Farmer, Krishi Officer
Priority 	High 

FR-03	Estimate areas possible paddy production 
Description 	Krishi Officer need to estimate possible paddy production in certain area in order to reach Govt. paddy buying goal.
Stakeholders 	Farmer, Krishi Officer
Priority 	High 

FR-04	Distribute paddy collection ward wise 
Description 	Krishi Officer need to distribute paddy collection to ward through union chairman
Stakeholders 	Farmer, Krishi Officer
Priority 	High 

FR-05	Dashboard  
Description 	Krishi Officer can see the total buying goal and achieved goal along with all farmer list.
Stakeholders 	Farmer, Krishi Officer
Priority 	Medium 

FR-06	Statistics 
Description 	Krishi Officer can see previous years paddy buy related statistics
Stakeholders 	Krishi Officer
Priority 	Medium  

FR-06	Update notice board
Description 	Krishi Officer can update notice board
Stakeholders 	Farmer, Krishi Officer
Priority 	Medium  

FR-07	Distribute rest amount of paddy to millers 
Description 	Krishi Officer can distribute rest amount of paddy of each farmer to millers.
Stakeholders 	Farmer, Krishi Officer, millers
Priority 	High 

   2.1.3 Retailer
FR-01	Login and Logout 
Description 	Retailer will be able to login and logout to the system with valid user credentials.
Stakeholders 	Retailer
Priority 	High 

FR-02	Search 
Description 	Retailer can search crops like vegetables for buying from farmers.
Stakeholders 	Retailer , Farmer
Priority 	High 

FR-03	Order crops 
Description 	Retailer can order for crops in selected crops.
Stakeholders 	Retailer, Farmer
Priority 	High 

FR-04	Payment  
Description 	Retailer can pay money for ordered crop through this system or can pay cash on delivery.
Stakeholders 	Retailer, Farmer
Priority 	Medium  

  
2.2	Non Functional Requirement 
2.2.1	Performance Requirements
Server software does not require any special hardware other than the minimum hardware required for running enterprise OS. Extra disk storage will be required for archives and electronic documents. Increases of memory enables efficient query processing, which is required for quick bibliographic search. Two server grade processors with clock speed 3.0 Ghz, at least 4GB RAM and 300 GB hard disk is recommended for the server. Client machine with recommended hardware required for desktop operating system and web browser.
2.2.2	Safety Requirements
As per IIT work place safety rules and the IIT server room where the server is supposed to be placed and the monitoring people.

2.2.3	Security Requirements
Each time there is a security violation, the log file will be updated with the login, date, and time. Again, high level cryptography and checking should be kept to make it more secured. However, while email or request from any unwanted client the request should drop and let that user know about the fault.
    2.2.4   Maintainability Requirements
At least one backup server with same configuration as in main server is also recommended for fault tolerance and better performance. Separate storage (with backup) for database, electronic document, and manuscript is also recommended. Multiple computing nodes with the storage are required for high availability and to enhance the performance of the application. Again, after a certain period the preliminary manuscript files and other files related with that can be deleted manually from the database to increase the performance.


3. Use Case Diagram:
3.1	Farmer’s use case diagram 
Fig 1: Use Cases – Farmer

Use Case No.	1.1
Use Case Name	Log in
Actor	Farmer
Description	Allowing farmer to login into the system
Precondition	Registration and user should remain in the login page
Trigger	Click the login link
Flow of Events	Two text fields to give input of the username and password respectively
Write the username and password on that field and
click the login button
Post Condition	User logged into the system

Use Case No.	1.2
Use Case Name	View Notice Board
Actor	Farmer
Description	Allowing farmer to see the Notice Board
Precondition	Login
Trigger	Click the Notice Board link
Flow of Events	From Menu in the Home page Farmer will click Notice Board
Post Condition	User sent to Notice Board 

Use Case No.	1.3
Use Case Name	Upload this season’s crop details
Actor	Farmer
Description	Farmer will fill the ‘crop details form’ for the admin.
Precondition	Login
Trigger	Click the ‘this season’s crop’ link
Flow of Events	From Menu in the Home page Farmer will click ‘this season’s crop’
Post Condition	User sent to ‘this season’s crop’  form to submit about this farming.

Use Case No.	1.4
Use Case Name	Ask query
Actor	Farmer
Description	Farmer will ‘Ask query’ to the krishi officer.
Precondition	Login
Trigger	Click the ‘Ask query’ link
Flow of Events	From Menu in the Home page Farmer will click ‘Ask query’
Post Condition	User sent to ‘Ask query’ form to ask about query.

Use Case No.	1.5
Use Case Name	Sell Crops
Actor	Farmer
Description	After govt. buys his share the farmer will sell the rest to mill owners or other places
Precondition	Login, sell to govt. his share.
Trigger	Click the ‘Sell Crops’ link
Flow of Events	From Menu in the Home page Farmer will click ‘Sell Crops’
Post Condition	User sent to ‘Sell Crops’ page to advertise about crops and offers.


3.2	 Govt. Officers use case diagram:
Fig 1 : Use Cases – Govt. Officer

Use Case No.	2.1
Use Case Name	Log in
Actor	Govt. Officer
Description	Allowing Krishi Officer to login into the system
Precondition	Registration and user should remain in the login page
Trigger	Click the login link
Flow of Events	Two text fields to give input of the username and password respectively
Write the username and password on that field and
click the login button
Post Condition	Govt. Officer logged into the system

Use Case No.	2.2
Use Case Name	Validate Farmer Registration
Actor	Govt. Officer
Description	Confirming Farmers registration information
Precondition	Farmer Must request to register first.
Trigger	Choose request from notification.
Flow of Events	After farmer’s request to register a notification will arise at krishi officer’s tab; asking his to confirm this farmer.
Post Condition	Go to farmer Profile Page
Use Case No.	2.3
Use Case Name	Estimate Areas Possible Crop Collection
Actor	Govt. Officer
Description	Farmer will inform what type of crop he is going to cultivate and with other agricultural researches krishi officer will estimate the possible crop growth.
Precondition	He must check farmer’s field physically and farmer must mention crop detail and land detail and pesticide and fertilizer he is using all kind of details.
Trigger	When farmer request in time of cutting crops.
Flow of Events	When farmer request to monitor before cutting his crops. He physically monitors and updates the data
Post Condition	Fill the next farmers form.

Use Case No.	2.4
Use Case Name	Distribute WARD Wise
Actor	Govt. Officer
Description	District Commissioner will distribute upazilla wise and they pass down the calculation ward-wise to farmer-wise.
Precondition	Send survey data to DC first.
Trigger	When DC confirms distribution.
Flow of Events	After sending the possible crop collection details the DC will calculate required and available crops and send order to upazilla. 
Post Condition	Distribution order reach field-agents.
Use Case No.	2.5
Use Case Name	Distribute The rest to mill owners
Actor	Govt. Officer
Description	District Commissioner will distribute upazilla wise and they pass down the calculation ward-wise to farmer-wise. The rest will be distributed among mill-owners.
Precondition	Complete Govt. requirement first.
Trigger	When Govt. quota Fills.
Flow of Events	After sending the possible crop collection details the DC will calculate required and available crops and send order to upazilla. The rest will be distributed among mill-owners.
Post Condition	Distribution order reach mil-owners.

Use Case No.	2.6
Use Case Name	Dashboard
Actor	Krishi Officer
Description	District Commissioner will distribute upazilla wise and they pass down the calculation ward-wise to farmer-wise. The rest will be distributed among mill-owners.
Precondition	Complete Govt. requirement first.
Trigger	When Govt. quota Fills.
Flow of Events	After sending the possible crop collection details the DC will calculate required and available crops and send order to upazilla. The rest will be distributed among mill-owners.
Post Condition	Distribution order reach mil-owners.
Use Case No.	2.7
Use Case Name	Update Notice
Actor	Krishi Officer
Description	Preparing notice about latest govt. facilities and offers and uploading them on notice board.
Precondition	Receive higher authority’s order.
Trigger	When receives order from senior officer.
Flow of Events	The District Commissioner updates the notice board.
Post Condition	Notice board updated and all user below receives a notification.

Use Case No.	2.8
Use Case Name	Check Statistic
Actor	Krishi Officer
Description	Officer might need to check the history/statics about reports like last year’s collection report or statistic about other necessary data.
Precondition	Previous year’s data must be available.
Trigger	When the ‘Check Statistics’ button is clicked.
Flow of Events	In the menu bar the check statistics button is there. And from the previous year’s database system will generate Charts and graphs.
Post Condition	Graph about real time data will be shown.

Use Case No.	2.9
Use Case Name	Response Farmer’s Query
Actor	Krishi Officer
Description	Farmer might ask a question about farming and govt. facilities and krishi officer will response them.
Precondition	Farmer ask a question.
Trigger	When farmer click submit query.
Flow of Events	Farmer’s query will open a reply option for krishi officer.
Post Condition	Query will be marked as answered.


3.3	Miller use case diagram:  
Fig. : Use Cases – Miller

Use Case No.	3.1
Use Case Name	Log in
Actor	Retailer
Description	Allowing Retailer to login into the system
Precondition	Registration and user should remain in the login page.
Trigger	Click the login link
Flow of Events	Two text fields to give input of the username and password respectively
Write the username and password on that field and
click the login button
Post Condition	Retailer logged into the system

Use Case No.	        3.2
Use Case Name	Search 
Actor	Retailer
Description	After govt. officials buys it’s share the retailers will search and offer the farmer to buy their crops. 
Precondition	Admin approves and limits their buying limit.
Trigger	When Search button is clicked.
Flow of Events	The farmers will advertise their remaining crops for the retailers to buy. 
Post Condition	Advertises will be shown.

Use Case No.	        3.3
Use Case Name	Order
Actor	Retailer
Description	Farmer and retailer will reach a deal between themselves and retailer will order the crops. 
Precondition	Farmer’s approval.
Trigger	When the order button is clicked.
Flow of Events	The farmers will advertise their remaining crops for the retailers and they make the deal. 
Post Condition	Crops will be ordered and advertise will be removed.

Use Case No.	        3.4
Use Case Name	Payment
Actor	Retailer
Description	After the deal they reached then the retailer make the payment. 
Precondition	Ordered.
Trigger	When Payment button is clicked.
Flow of Events	Choose the suitable payment method. 
Post Condition	Payment is done.

