# Selenium Testing

A project for using selenium testing, and using Page Object Model design pattern.

## Running the tests

### Requirements

- Docker
- A supported webdriver (Firefox, Chrome, Edge...)

### Instructions (Backend/Frontend)
Repo for Backend and frontend:
```
https://github.com/Ominousity/Mockly-Selenium
```

Create a new dockerized mssql database using the below command (dont change any parameters)

```
docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=pvg@zeq4RWQ3wxr-rhn' -p 1433:1433 --name sqlserver -d mcr.microsoft.com/mssql/server:2019-latest
```

When the mssql server is up and running you need to create a new database on it called "Endpoints", after that create a DB migration for it so it has the correct tables, it is done as follows:

open powershell in the WebAPI Project and write the following commands:

```
dotnet ef migrations add <name>
dotnet ef database update
```

after that is done you can run the WebAPI, for the frontend it is run by calling the following command in this directory of the repository:

Frontend > mockapi

```
npm i
npm run dev
```

now both the frontend and backend should be working and the website be functional

### Instructions (Selenium tests)

To run the selenium test yopu first need to create a virtual envronment in the root directory with the command:

```
python -m venv .venv
```

you can then enter the virtual envronment like this:

```
.venv/scripts/activate
```

and install the necesarry libraries with this command:

```
pip install -r requirements.txt
```

and run the tests with:

```
python -m unittest discover
```