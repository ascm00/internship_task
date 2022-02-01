# This is a sample Python script.
import json
import os

from _datetime import datetime, timedelta
import statistics




def count_unique_users(directory):
    """Counts unique users"""

    users = set() #only unique values in set

    json_files = [j_file for j_file in os.listdir(directory)]


    for file in json_files:
        json_file = open(directory + '/' + file, "r")
        data = json.load(json_file)


        for user in data.keys():
            users.add(user)

    return len(users)



def count_unique_items(directory):
    """Counts unique items"""

    items = set()

    json_files = [j_file for j_file in os.listdir(directory)]

    for file in json_files:

        users = set()

        json_file = open(directory + '/' + file, "r")
        data = json.load(json_file)

        for user in data:
            users.add(user)


        for u in users:
            for x in data[u].keys():
                if x != 'variant':
                    items.add(x)



    return len(items)


def list_of_timedeltas(directory):
    """Returns a list of timedeltas between requests, then we can count average and median"""


    json_files = [j_file for j_file in os.listdir(directory)]

    for file in json_files:

        users = set()

        json_file = open(directory + '/' + file, "r")
        data = json.load(json_file)

        for user in data:
            users.add(user)

        timedeltas = list()

        for u in users:
            for x in data[u].keys():
                if x != 'variant':
                    for item in data[u][x]:
                        if len(item) == 2:
                            timedeltas.append(datetime.fromisoformat(item[1][0]) - datetime.fromisoformat(item[0][0]))

    return timedeltas

def count_avg_time():
    """Counts average time between requests"""

    timedeltas = list_of_timedeltas('data')

    average_timedelta = sum(timedeltas, timedelta(0)) / len(timedeltas)

    return average_timedelta


def count_median_time():
    """Counts median time between requests"""

    timedeltas = list_of_timedeltas('data')

    median_timedelta = statistics.median(timedeltas)

    return median_timedelta


def maximum_request_number(directory):



    json_files = [j_file for j_file in os.listdir(directory)]

    for file in json_files:


        json_file = open(directory + '/' + file, "r")
        data = json.load(json_file)

        for user in data:
            for item in data[user].keys():
                if item != 'variant':
                    for x in data[user][item]:
                        if "similarInJsonList" in x:
                            print(x)









def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':

    print("Number of unique users: ")
    print(count_unique_users('data'))

    print("Number of unique requests: ")
    print(count_unique_items('data'))

    print("Average time: ")
    print(count_avg_time())

    print("Median time: ")
    print(count_median_time())

    #print(maximum_request_number('data'))

