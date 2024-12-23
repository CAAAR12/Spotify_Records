"""This module is intended to host funcitons to add to the registery for the RFID card."""
import pandas as pd
import csv

support = "registry.csv" #for now the csv is local, will change once database is uploaded

def readRegistry(database:str):
    """
    This function reads the registry, where the Spotify URI is the main way of IDing.
    For demo purposes, this will be csv file. As the application matures, this should
    become reading from an SQL database. 
    """
    try:
        dataframe = pd.read_csv(database).set_index('URL')
        return dataframe
    except FileNotFoundError as e:
        return e
   
def findItem(database:pd.DataFrame, item:str):
    """
    Retrieves the RFID Code of the item. If it does not exist, then return nothing.
    """
    try:
        RFID = database.at[item,"RFID Code"]
        return str(RFID)
    except KeyError as e:
        return None

def Add2Registry(database:str,URL,type="BLANK",name="BLANK",RFID="TEMP"):
    """
    Be able to add to the registry an item from Spotify.
    The RFID tag can be added seperately. If it is present though
    then add it to the registry automatically.
    """
    #Columns of the CSV file are as follows:
    #Type, Name, URI, RFID Code
    with open(database,'a') as fd:
        writer = csv.writer(fd)
        writer.writerow([type,name,URL,RFID])
    
    #Fetch updated CSV file
    updatedData = readRegistry(database)

    if findItem(updatedData,URL):
        return updatedData
    else:
        return None
