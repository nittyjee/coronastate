

# The CoronaState Project
We are creating a single source for all covid-19 cases.
<br>
All cases globally, located as locally as possible.
<br>
Apparently we’re the only ones attempting to take the responsibility of doing this.

We currently draw from about 40 sources:
<br>
https://docs.google.com/spreadsheets/d/1FH8jc-wqf4tPsj3vSVWKi2bh-0VsramTDAAqJFNoEo0/

**Map:** [http://coronastate.org/](http://coronastate.org/)


## Contribute

We could really use your help or participation, in any way you want.

- **Join our Discord for anything you want to discuss, and for mapping and development:** <br>
https://discord.gg/CCGVMUy

- **Contribute to data development:** <br>
We need people to find new datasets and add to our list, and for people to develop or use our code to add it to our database.
This is our ongoing list of needs: <br>
https://docs.google.com/document/d/1QAzJDlGk4sYjfQngZ3gDFJJhM_D2tgFeA8U94djy2iA/edit

- **Contribute to site app development:** <br>
Our map and data visualization is innovative, and there are a ton of things we need to have done:
https://docs.google.com/document/d/1mLC5qk2NtfW6E8D21erk8ovEDyr2XjZ8EaR3IO9xsj0/edit <br>
. <br>
**Site application repo:** <br>
https://github.com/nittyjee/coronastate_map

- **Donate:** [Gofundme Campaign](https://www.gofundme.com/f/coronastate-project-all-covid19-data-in-one-place)



## How CoronaState Works

For each dataset we:
- Fork or create a data feed
- Process the data into common csvs for each admin level (eg one csv for countries, one for state/provinces, and so on): <br>
https://github.com/nittyjee/coronastate/tree/master/data/layers
- Have the raw data as csvs (see also source spreadsheet above): <br>
https://github.com/nittyjee/coronastate/tree/master/data/rawdata/data
- Any new places are automatically geocoded
- As the data updates, the map updates, every 20 mins.





# About CoronaState

## First, how does this compare to what others are doing?

  

Some efforts to map data, like the John Hopkins University (JHU) Dashboard, have done an excellent job of combining and updating data from around the world, and we are incorporating their data, and creating a vastly expanded database that they can in turn use.

  

Most global data and mapping efforts have combined data from centralized sources in each country, and some have data for some countries at a level lower (eg. states and provinces). We have combined several datasets at that level, which can be used, and are prepared to go to a much more local level.

We also have a map that shows how infections spread over time, and has effective visualization that renders quickly.

## How is this useful to people?

Locating infections at all levels is absolutely essential. People can know where it is in order to fight it and defend themselves against it.

### Defending yourself:

If people didn’t have maps, like the JHU Dashboard, they would be lost, and efforts to map locally have been a great success. In South Korea, a very successful app was developed that allowed people to see how close they were in the vicinity of infections, anywhere someone was. With Coronastate we can get local data, so people can go anywhere in the world.

### A Powerful Tool For Epidemiology:

Locating diseases is fundamental to epidemiology. Modern epidemiology was partly born when a map was produced of cholera clusters around a water source. All cases are local, and patterns emerge from maps.

The benefit of this project can go much beyond covid-19 and be used for any health issue and future epidemics. We will create knowhow and expertise and tools for doing so.

## What about privacy?

Knowing who is infected is a stigma that is dangerous to someone and their friends and family, and their rights must be respected. We will make sure that data will be as local as possible, while making it in a wide enough area where it’s difficult or impossible to find a person infected, or people around them.
  

## How are you doing this?

  

Our goals are finding, listing, and internalizing all available datasets as far back as possible, updating them as they are, from their original sources. We are adding coordinates to all locations and verifying them (geocoding). The raw data will be shown and processed into common formats. We are finding lists of individual cases and would like to develop databases and map them.

  
  
## What have you done so far?

So far we have combined over a dozen datasets of every country at multiple administrative levels. So far most countries outside of Africa have two levels, and a dozen countries have three levels, a couple have more.

We’ve created a map of all locations we have that updates every 20 minutes, with a timeline going back to the first cases.

Here is our map: [http://coronastate.org/](http://coronastate.org/)

We currently draw from about 40 sources:
<br>
https://docs.google.com/spreadsheets/d/1FH8jc-wqf4tPsj3vSVWKi2bh-0VsramTDAAqJFNoEo0/

Here is a csv of every place with the date of its most recent cases, and the sources:
<br>
[https://github.com/nittyjee/coronastate/blob/master/data/most_recent.csv](https://github.com/nittyjee/coronastate/blob/master/data/most_recent.csv)



  
  

## Are you visualizing the data?

  

While centralizing data is our aim, we have to verify it in visualizations, because it’s only useful if it’s visualized, with maps and graphs. We are attempting to find the best data visualizations to use for our data, and people are welcome to use our data for theirs. We have our application available for people to use or embed around online. We encourage others to develop their own, and we can link to it. The project will also benefit the world by making the applications available for use for any project.

  
  

## What else would you like to do?

  

We would like to go into detail about where people were infected, from whom, and how they traveled. This could be done in a database, but can be animated visually. This can give us all an idea of how the disease actually traveled, and possibly develop or expand the use of tools used for epidemiology.

  

It would be great if we could incorporate modeling with graphs and scenarios at all levels, the epidemic globally and in cities and communities. It would also be good to model how the disease would have spread if actions weren’t taken. This would take research and invite people who do that sort of work.

  


## How can I help?

Besides funding and donating, we can use plenty of volunteers for everything. You can help us with:
- Tell us about new datasets to add to our list.
- Application and data visualization development.
- Data development.
- Raise funding.
- Suggestions and comments
- Join discussions (we will have a slack channel and possibly a forum soon).


## What do you need to make this happen?

We need funding. A serious effort like this cannot be done only with volunteers. Now that we’ve demonstrated success, we need sustained, dedicated coordination and people to gather data. We also need developers for our data visualizations. Furthermore, in order to provide the project to epidemiologists for future work, we need to have it engineered for them to use and implement. The work we have already done is significant, and we can do our work very rapidly and efficiently if we are enabled.

Here are our current funding tiers:

- $5,000: Develop basic data visualizations and process comprehensive datasets.
- $15,000: Show projections over time, and begin coordinating volunteers to gather and map data at a very local level.
- $25,000: Gather data at a very local level, country by country. Further map visualizations of movement and transmission.

Donate to our current Gofundme Campaign:

[https://www.gofundme.com/f/coronastate-project-all-covid19-data-in-one-place](https://www.gofundme.com/f/coronastate-project-all-covid19-data-in-one-place)

![enter image description here](http://coronastate.org/github_images/asdf.jpg)

## Contact Us

Email us for anything:
<br>
info@coronastate.org

## Creators

### Director:

|  |  |  |  |
|--|--|--|--|
|![enter image description here](http://coronastate.org/github_images/nitin.jpg)|Nitin Gadia|New York City, USA|Nitty Gritty Multimedia<br>thenittygritty.org/me

### Head Developer:
|  |  |  |  |
|--|--|--|--|
|![enter image description here](http://coronastate.org/github_images/hima_kallam_small.jpg)|Hima Kallam|Folsom, California, USA|Data Processing<br>Tileset Automation<br>Dataviz<br>Web Interface

### Developers:

|  |  |  |  |
|--|--|--|--|
|  ![enter image description here](http://coronastate.org/github_images/dadior.jpg)|Dadior Chen|Beijing, China|Data Processing|
|  ![enter image description here](http://coronastate.org/github_images/arsen.jpg)|Arsen Kocharyan|Yerevan, Armenia|Web Interface|
|  ![enter image description here](http://coronastate.org/github_images/santiago_small.jpg)|Santiago Nullo|Buenos Aires, Argentina|Web Interface|
