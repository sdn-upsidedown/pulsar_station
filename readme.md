# PULSAR STATION

**Date** : 23/05/2021

**Auteurs** : Anatole de Chauveron

**Groupe** : Upside Down

**Version** : 3.0.0

**Confidentialité** : Tous droits réservés

### Adresse du Git 

**GIT** : https://github.com/sdn-upsidedown/pulsar_station.git

The pulsar station project is a student project where we have to create a meteorological station, and predict the weather with high accuracy thanks to the data that we sendt with the station.

This project is related to the physical station.

## Install and run project

In order to update the code you need to have the Pymakr extension on Vscode.

Make sure to disable your Bluetooth as it can interfer with the Ports.

## Workflow description

The project is composed with multiples modules that manages different parts of the station:

**data :**

Manages the data (wright, read and reset the datas).

**lib :**

A library of assets in order to user the Pysense sensors.

**sensors :**

Functions to get datas.

**states :**

Manages the state of the station (battery, cpu, voltage...).

**station :**

Manages the station configuration (init, shutdown, conf...).

**station_network :**

Manages the station connection to Network and APIs (internet, data transfer...).

**utils :**

A set of tools for the modules (date, interface...)


## Station functionnality

### On boot

The station initiate herself, every ten minutes by looking inside the conf files. It will try to connect to Internet as well.

It is then directed to the main.

### Main

Register a set of data, and the current station status.

### Data transfer

Every 6 datas (one hour), the datas are beeing send to the API. If the operation succeeded, the datas are beeing deleted. Otherwise, they are kept until the transfer to the API worked.