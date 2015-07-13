My name is Corinne Fukayama and I am looking at being able to predict the general health for women. That’s kind of broad, so let’s narrow that down.

###**What's the problem?**###

My problem looks at two forces at play:

The first is that, quite simply, as you get older your health gets worse. 

The second is related to the weathering hypothesis, which postulates that the health of Af Am women gets worse earlier in adulthood as a consequence of cumulative socioeconomic disadvantage.

So my question becomes: can we predict an adult women’s general health based on existing structural disadvantages such as race and SES, and related, can we predict the change in health over time?

This is something that’s become important as precision medicine becomes more relevant, since that’s looking at not just your genes but your environment and lifestyle to tailor a specific treatment plan.

###**How can you measure "general health"?**###

So you may be wondering “that’s cool but how do you measure general health? Is it the absence or presence of disease, what is it?”

Researchers have been using something called “allostatic load” in an attempt to scientifically represent the “wear and tear” on the body as a function of repeated exposure to stress. They do this using a composite function based on a variety of biomarker scores, and the biomarkers used depends on the study and what information gets collected in the study. Generally it follow four general categories, which I’ve listed along with some example biomarkers from those categories.

###**Where am I getting the data?**###

Data collection for this project is relatively easy– there’s something called the SWAN health data set, which stands for the Study of Women’s Health Across the Nation. It’s a 21 year and counting multi-site longitudinal and epidemiological study that focuses on the quality of life during aging.

What this means is that 3,302 subjects have been continually assessed every 2 years starting in 1994. Their assessment includes biological tests such as blood tests and measuring height and weight as well as surveys and questionnaires that measure more psychological and social changes. Currently there are 12 data sets available to the public, ranging from 1994-2008.

###**Data Exploration**###

Each assessment collects between 500-700ish variables of data, and this does not include the Cross-Sectional and Baseline data set that collects different demographic information.

Since I'm looking at Race and SES as "indicators" for health outcomes, I can find the basic race, education, income, and marital status demographic indicators that are common in health studies. However with the amount of information in the study, I can dig deeper into the other mediating variables of Race and SES, such as 

**Discrimination** (using the Detroit Area Study Everyday Discrimination Scale, which asks questions such as You are treated with less courtesy than other people, you are treated with less respect than other people, you are treated different at restaurants with often, sometimes, rarely, never)

**Perceived Stress** (using a shortened version of the Perceived Stress Scale which asks questions such as whether you felt unable to control important things in your life)

**Hostility** (Cooke Medley Questionnaire, T/F, I have often had to take orders from someone who did not know as much as I did)

And then my allostatic load outcome, which is dependent on the 11 measures I've listed there.

###**Data Exploration part 2**###

Most of my time has been spent crawling through the codebooks and lit research trying to determine which variables and fields are representative of what I want to do. Now armed with a better idea of which fields I want to use, I've been able to start playing around with the data.

**The bad issues**
- So the very first thing I noticed when I imported all of the data sets was that the shape was different for every visit. There was loss to follow-up and not all information was recorded for every participant in every site visit
- For example, in Visit 2, 6 out of the 11 fields I want to use to calculate allostatic load were not recorded for every participant, while for Visits 4-7, the questionnaires that looked at structural disadvantages was absent.

**The good issues**
So despite this, there are actually some really good things about these data sets. The main one being is that all of the data sets are relatively clean-- I haven't come across any user inputted errors, and everything is an integer. The only issue I've come across is that missing values are coded as spaces.

###**Next Steps**###

So because of the missing data, I'm going to have to do some imputation in order to be able to continue with my calculations. I'm also trying to determine whether the missing data on structural disadvantages actually matters-- my hypothesis is that those scores and measures won't vary significantly over time, and if so I might just use what I can measure at baseline.

Finally I need to determine the appropriate features to include in the model. I'm looking at the pathways that Race and SES affect health. From a behavioral health standpoint, it's really simplistic to say that race and SES directly affects health. A lot of research has indicated that there are mediating variables such as discrimination, perceived stress, and hostility that are influenced by Race and SES and then affect health so I want to be able to investigate that pathway and determine whether or not its significant to the model.
