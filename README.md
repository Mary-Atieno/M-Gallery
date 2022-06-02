# PROJECT NAME

M-GALLERY

## AUTHOR

MARY ATIENO

## DESCRIPTION

A personal gallery made using Django that displays images of different types of things and allows people to see them.

## Features

As a user of the application you will be able to:

View different photos that interest you.

Click on a single photo to expand it and also view the details of the photo. The photo details will appear on a modal within the same route as the main page.

Search for different categories of photos. (ie. Travel, Food)

Click on share icon to share the image with any of your social account or alternatively Copy a link to the photo and share with your friends.

View photos based on the location they were taken or category.

## Installation and setup instructions

Clone this repo: git clone <https://github.com/Mary-Atieno/M-Gallery.git>
The repo comes in a zipped or compressed format. Extract to your prefered location and open it.

open your terminal and navigate to gallery then create a virtual environment.For detailed guide refer here

To run the app, you'll have to run the following commands in your terminal

pip install -r requirements.txt
On your terminal,Create database gallery using the command below.

CREATE DATABASE gallery;
Migrate the database using the command below

python3 manage.py migrate
Then serve the app, so that the app will be available on localhost:8000, to do this run the command below

python manage.py runserver
Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.

Running the tests
Use the command given below to run automated tests.

    python manage.py test gallery

## TECHNOLOGIES USED

Django - web framework used

Javascript - For DOM(Document Object Manipulation) scripts

HTML - For building Mark Up pages/User Interface

CSS - For Styling User Interface

## CONTACTS

maryatieno@gmail.com

## LIVE LINK

Find the deployed app: here

## LICENSE

MIT

Copyright (c) 2022 mary atieno

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
