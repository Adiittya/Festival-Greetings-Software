
# Festival Greetings Software

This project is a customer engagement system that sends personalized birthday greetings and festival wishes based on regional preferences. It includes features such as database connectivity, automated birthday greetings, loyalty points-based rewards, email notifications during regional festivals, customer segmentation, and a user-friendly GUI. It is designed to foster stronger connections with customers and enhance their loyalty.

Additionally, the project offers database connectivity, allowing businesses to seamlessly manage customer data. This feature enables efficient storage, retrieval, and management of customer information, ensuring that the system has access to the most recent data for personalized greetings and festival wishes.






## Features

- Database Connectivity
- Festival Greetings
- Automated Birthday Greetings
- Loyalty Points-Based Rewards
- Customer Segmentation
- User-Friendly GUI


## Deployment

To download all the necessary libraries, you can follow these steps:

1.Navigate to the directory where your requirements.txt file is located.

Run the following command:

```bash
  pip install -r requirements.txt

```
**To use the SQL file:**

1.Open phpMyAdmin in your web browser.

2.Log in to phpMyAdmin.

3.Go to the "Import" option.

4.Choose the SQL file **main.sql** and select any desired settings.

5.Click "Go" or "Import" to initiate the import process.

6.Wait for the import to finish.

7.Verify that the database tables and data were created successfully.

Assuming you're using XAMPP or a similar local development environment with an admin panel and ensure that both the Apache and MySQL services in XAMPP are started before attempting to access the admin panel.

***IMPORTANT NOTE***

Modification in Code after Successful Registration

After successfully registering yourself, you need to make a change in the code. Go to line 674 in the register.py file and modify it from Res = Register() to Log = Loginapp(). This change resolves an issue with the "Already Registered" button in the GUI, and it will be resolved in the future. However, until then, please follow this method.

at line 674
```bash
  Res=Register()

```
to 

```bash
  Log=Loginapp

```

**FOR SENDING MAILS**

1.In the **mail.py** file, follow these steps for deployment:

2.Open the file and locate the section for email credentials.

3.Replace the placeholder email ID with your own email ID.

4.Instead of using your regular Google account password, generate an app password.

5.Go to your Google Account settings, find "App Passwords" or "Manage app passwords".

6.Generate a new app password for your application and copy it.

7.Replace the placeholder password in the mail.py file with the generated app password.

8.By doing this, you will use a specific app password for secure email authentication in your project.







## Appendix

1.How to Run the Project

Ensure that all the required modules are in the same directory, as the project is dependent on these modules. Run the **Register.py** file to register yourself. This will store your record in the database. After registration, use your credentials to log in.

2.Customer and Festival Records

You will find customer and festival records within the project. You can modify the data from the GUI interface provided.

3.CSV to SQL File

There is a file called **csvtosql.py** which can be used to upload data from a CSV file to the database. You can modify the festival file according to the festivals you need or prefer.

4.Festival Greetings and Images

5.Whenever a user logs in, the system will check for upcoming festivals and birthdays. Based on this information, it will send personalized emails to clients. You can also change the images according to your preference. Just ensure that the festival ID matches the name of the corresponding image file, for example, **12.jpg**
## FAQ

1.Mail.py giving error password not matched

In the mail.py file, if you encounter an error stating that the password is not matched, it's important to note that using your regular Google account password directly is not recommended for security reasons. Instead, you should generate an app password specifically for your project.

You can watch here how to do it 

https://youtu.be/hXiPshHn9Pw



## License

[MIT](https://choosealicense.com/licenses/mit/)


## Feedback

If you have any feedback or quries, please reach out to me at adityahakani29@gmail.com

