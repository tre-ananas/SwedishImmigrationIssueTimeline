##### SETUP #####
#####
#####

### Packages
###

# Load Packages
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

### Data
###

# Load data
plotting_data = pd.read_csv('plotting_data.csv')
election_data = pd.read_csv('election_data.csv')
variable_definitions = pd.read_csv('plotting_variable_definitions.csv')



##### MAIN FUNCTION ######

def main():
    # Set up the layout
    st.set_page_config(
        page_title="Swedish Immigration Issue",
        page_icon=":rocket:",
        layout="wide"
    )

    ##### SIDEBAR #####
    #####
    #####

    ### Year Selection ###
    ###

    # Dropdown menu for selecting year
    selected_year = st.sidebar.selectbox('Select Year:', plotting_data['Year'])

    ### Election Results ###
    ###

    # Election Data
    election_results_data = {
    2010: pd.DataFrame({
        'Party': ['Social Democrats', 'Moderates', 'Greens', 'Liberals', 'Center', 'Sweden Democrats', 'Left', 'Christian Democrats', 'Other'],
        # 'Votes': ['1,827,497', '1,791,766', '437,435', '420,524', '390,804', '339,610', '334,053', '333,696', '85,023'],
        # 'Vote %': [30.7, 30.1, 7.3, 7.1, 6.6, 5.7, 5.6, 5.6, 1.4],
        'Seats': [112, 107, 25, 24, 23, 20, 19, 19, 0],
        'Growth': [-18, 10, 6, -4, -6, 20, -3, -5, 0],
        'Class': ['Friendly', 'Friendly', 'Friendly', 'Friendly', 'Friendly', 'Hostile', 'Friendly', 'Friendly', 'NA']
        }),
    2014: pd.DataFrame({
        'Party': ['Social Democrats', 'Moderates', 'Sweden Democrats', 'Greens', 'Center', 'Left', 'Liberals', 'Christian Democrats', 'Other'],
        # 'Votes': ['1,932,711', '1,453,517', '801,178', '429,275', '380,937', '356,331', '337,773', '284,806', '255,045'],
        # 'Vote %': [31.0, 23.3, 12.9, 6.9, 6.1, 5.7, 5.4, 4.6, 4.1],
        'Seats': [113, 84, 49, 25, 22, 21, 19, 16, 0],
        'Growth': [1, -23, 29, 0, -1, 2, -5, -3, 0],
        'Class': ['Friendly', 'Friendly', 'Hostile', 'Friendly', 'Friendly', 'Hostile', 'Neutral', 'Friendly', 'NA']
        }),
    2018: pd.DataFrame({
        'Party': ['Social Democrats', 'Moderates', 'Sweden Democrats', 'Center', 'Left', 'Christian Democrats', 'Liberals', 'Greens', 'Other'],
        # 'Votes': ['1,830,386', '1,284,698', '1,135,627', '557,500', '518,454', '409,478', '355,546', '285,899', '99,137'],
        # 'Vote %': [28.3, 19.8, 17.5, 8.6, 8.0, 6.3, 5.5, 4.4, 1.6],
        'Seats': [100, 70, 62, 31, 28, 22, 20, 16, 0],
        'Growth': [-13, -14, 13, 9, 7, 6, 1, -9, 0],
        'Class': ['Friendly', 'Friendly', 'Hostile', 'Friendly', 'Friendly', 'Friendly', 'Friendly', 'Friendly', 'NA']
        }),
    2022: pd.DataFrame({
        'Party': ['Social Democrats', 'Sweden Democrats', 'Moderates', 'Left', 'Center', 'Christian Democrats', 'Greens', 'Liberals', 'Other'],
        # 'Votes': ['1,964,474', '1,330,325', '1,237,428', '437,050', '434,945', '345,712', '329,242', '298,542', '100,076'],
        # 'Vote %': [30.3, 20.5, 19.1, 6.7, 6.7, 5.3, 5.1, 4.6, 1.5],
        'Seats': [107, 73, 68, 24, 24, 19, 18, 16, 0],
        'Growth': [7, 11, -2, -4, -7, -3, 2, -4, 0],
        'Class': ['Hostile', 'Hostile', 'Hostile', 'Friendly', 'Friendly', 'Hostile', 'Friendly', 'Friendly', 'NA']
        }),
    }

    # Find the closest election year because not all years are election years
    closest_election_year = max(year for year in election_results_data.keys() if year <= selected_year)
    
    # Find the range of years for the election composition
    first_year = closest_election_year
    last_year = closest_election_year + 4


    ### News Links ###
    ###

    # News Links Data
    links_data = {
        'Link 1': {'year': 2013, 'title': 'Syrian Refugees Inbound', 'outlet': 'Financial Times', 'subtitle': 'Background information on Syrian immigration into Sweden.', 'url': 'https://www.ft.com/content/9752f8a6-6eeb-11e3-9ac9-00144feabdc0'},
        'Link 2': {'year': 2013, 'title': 'Islamic Fundamentalism Poll', 'outlet': 'Washington Post', 'subtitle': 'Insights into fundamentalist ideas amongst Muslims in Western European countries.', 'url': 'https://www.washingtonpost.com/news/monkey-cage/wp/2013/12/13/how-widespread-is-islamic-fundamentalism-in-western-europe/'},
        'Link 3': {'year': 2014, 'title': 'Mosque Set Ablaze', 'outlet': 'AlJazeera America', 'subtitle': 'An arson allegedly sets a mosque on fire in Eskilstuna, Sweden, injuring five.', 'url': 'http://america.aljazeera.com/articles/2014/12/25/swedish-mosque-setablaze.html'},
        'Link 4': {'year': 2014, 'title': 'Underlying Racial Tensions', 'outlet': 'AlJazeera America', 'subtitle': 'A progressive exploration of racial tensions and segregation in Sweden.', 'url': 'http://america.aljazeera.com/opinions/2014/6/sweden-refugees-racismstockholm.html'},
        'Link 5': {'year': 2014, 'title': 'Two Car Bombings', 'outlet': 'CTV News', 'subtitle': 'Two car bombs detonated in an immigrant-heavy district in Malmö.', 'url': 'https://www.ctvnews.ca/world/no-injuries-after-2-car-bombs-rock-swedish-city-of-malmo-1.2156901'},
        'Link 6': {'year': 2014, 'title': 'Child Refugees', 'outlet': 'AlJazeera', 'subtitle': 'A description of the successes, failures, and political ideas concerning immigration into Sorelse, Sweden.', 'url': 'https://www.aljazeera.com/features/2014/12/17/child-refugees-call-tiny-swedish-town-home'},
        'Link 7': {'year': 2015, 'title': 'Paris Attacks of 2015', 'outlet': 'Britannica', 'subtitle': 'A summary of the terrorist attacks that killed 130 people across Paris on November 13, 2015.', 'url': 'https://www.britannica.com/event/Paris-attacks-of-2015'},
        'Link 8': {'year': 2015, 'title': 'Charlie Hebdo Shooting', 'outlet': 'BBC', 'subtitle': 'A summary of the terrorist attack that killed 17 people in Paris from January 7-9, 2015.', 'url': 'https://www.bbc.com/news/world-europe-30708237'},
        'Link 9': {'year': 2016, 'title': 'Brussels Bombings', 'outlet': 'France24', 'subtitle': 'An account of the trials for the 8 men suspected of killing 32 people on March 22, 2016.', 'url': 'https://www.france24.com/en/europe/20230915-belgian-court-sentences-terrorists-behind-2016-brussels-bombings'},
        'Link 10': {'year': 2017, 'title': 'Stockholm Truck Attack', 'outlet': 'Politico', 'subtitle': 'A brief description of the terrorist attack that killed 4 in Stockholm on April 7, 2017.', 'url': 'https://www.politico.eu/article/suspected-stockholm-attacker-admits-to-terrorist-attack-crime-isis/'},
        'Link 11': {'year': 2017, 'title': 'Stockholm Attack Perpetrator', 'outlet': 'BBC', 'subtitle': 'Biographical sketch of Rakhmat Akilov, the Uzbek asylum seeker who perpetrated the April 7th attack.', 'url': 'https://www.bbc.com/news/world-europe-39552691'},
        'Link 12': {'year': 2016, 'title': 'Nice Truck Attack', 'outlet': 'France24', 'subtitle': 'An account of the trials for the 8 men suspected of killing 86 people on July 14, 2016', 'url': 'https://www.france24.com/en/europe/20221213-french-court-convicts-all-eight-suspects-over-2016-truck-attack-in-nice'},
        'Link 13': {'year': 2016, 'title': 'Munich Attack', 'outlet': 'DW', 'subtitle': 'An account of the shooting that targetted immigrants in Munich on July 22, 2016, killing 9.', 'url': 'https://www.dw.com/en/germany-2016-munich-attack-had-radical-right-wing-motives-say-police/a-50991641'},
        'Link 14': {'year': 2017, 'title': 'Manchester Arena Bombing', 'outlet': 'Counter Extremism Project', 'subtitle': 'Biographical sketch of Salman Abedi, who killed 22 people in a suicide bombing of a concert on May 22, 2017.', 'url': 'https://www.counterextremism.com/extremists/salman-abedi'},
        'Link 15': {'year': 2017, 'title': 'Barcelona Attacks', 'outlet': 'CNN', 'subtitle': 'A summary of the terrorist attacks that killed 13 people in Barcelona, Spain on August 17, 2017.', 'url': 'https://www.cnn.com/2017/08/17/europe/barcelona-las-ramblas-van-hits-crowd/index.html'},
        'Link 16': {'year': 2020, 'title': 'Hanau Shootings', 'outlet': 'The Guardian', 'subtitle': 'A summary of the "racially motivated" attack that killed 9 on February 19, 2020.', 'url': 'https://www.theguardian.com/world/2020/feb/19/shooting-germany-hanau-dead-several-people-shisha-near-frankfurt'},
        'Link 17': {'year': 2015, 'title': 'Prosecution of Swedish Terrorists', 'outlet': 'France24', 'subtitle': 'A summary of the prosecution of two Swedish citizens who aprticipated in "terrorist crimes" in Syria in 2013.', 'url': 'https://www.france24.com/en/20151214-sweden-sentenced-life-terrorist-syria'},
        'Link 18': {'year': 2015, 'title': 'Swedish Policies Tightening', 'outlet': 'Politico', 'subtitle': 'An analysis of immigration-related strains on Swedish resources and the resulting social and political backlash.', 'url': 'https://www.politico.eu/article/sweden-faces-moral-dilemma-over-migration-malmo-refugees-border-checks/'},
        'Link 19': {'year': 2015, 'title': '"Irresponsible" Swedish Policy', 'outlet': 'NY Times', 'subtitle': 'A critique of the open-border policies that opened the door to far-right groups in Sweden.', 'url': 'https://www.nytimes.com/2015/11/14/opinion/swedens-self-inflicted-nightmare.html'},
        'Link 20': {'year': 2015, 'title': 'Shifting Public Sentiment', 'outlet': 'The Telegraph', 'subtitle': 'An analysis of why anti-immigrant sentiments have risen in Sweden.', 'url': 'https://www.telegraph.co.uk/news/worldnews/europe/sweden/11992479/How-Sweden-the-most-open-country-in-the-world-was-overwhelmed-by-migrants.html'},
        'Link 21': {'year': 2015, 'title': 'Parties React to Harsher Policies', 'outlet': 'The Guardian', 'subtitle': 'Reactions from mainstream Swedish political parties regarding the tightening of immigration policies.', 'url': 'https://www.theguardian.com/world/2015/nov/24/sweden-asylum-seekers-refugees-policy-reversal'},
        'Link 22': {'year': 2015, 'title': 'Violent Identity Crisis', 'outlet': 'The New Yorker', 'subtitle': 'A summary of competing identities in Sweden, highlighted by an anti-immigrant attack at a school.', 'url': 'https://www.newyorker.com/news/news-desk/an-attack-and-an-identity-crisis-in-sweden'},
        'Link 23': {'year': 2014, 'title': 'Changing Tides in Sweden', 'outlet': 'NPR', 'subtitle': 'A description of recent election results and failing assistance policies in Sweden.', 'url': 'https://www.npr.org/sections/parallels/2014/12/05/368640533/swedens-tolerance-is-tested-by-tide-of-syrian-immigrants'},
        'Link 24': {'year': 2016, 'title': 'Sweden to Deport Asylum-Seekers', 'outlet': 'TIME', 'subtitle': 'Sweden intends to deport the 45 percent of asylum-seekers whose requests it rejected.', 'url': 'https://time.com/4197435/sweden-deport-asylum-seekers/'},
        'Link 25': {'year': 2016, 'title': 'Investigating Youth Assimilation', 'outlet': 'NPR', 'subtitle': 'A short summary of Swedish policy and experience with accepting and integrating young immigrants.', 'url': 'Sweden intends to deport the 45 percent of asylum-seekers whose requests it rejected.', 'url': 'https://www.npr.org/sections/parallels/2016/03/07/468589425/as-migrants-flow-in-sweden-begins-to-rethink-its-open-door-policy'},
        'Link 26': {'year': 2016, 'title': 'Fear Manifests Politically', 'outlet': 'NPR', 'subtitle': 'Increases in immigrant populations spark Swedish fears and an anti-immigrant political backlash.', 'url': 'https://www.npr.org/sections/parallels/2016/04/06/473261682/as-sweden-absorbs-refugees-some-warn-the-welcome-wont-last'},
        'Link 27': {'year': 2016, 'title': 'New Identity Checks', 'outlet': 'The Conversation', 'subtitle': 'Sweden implements identity checks on traffic between Sweden and Denmark to crack down on refugee inflow.', 'url': 'https://theconversation.com/why-is-sweden-tightening-its-borders-after-years-of-welcoming-migrants-53000'},
        'Link 28': {'year': 2016, 'title': 'Coverups for Asylum Seekers', 'outlet': 'TIME', 'subtitle': 'Swedish police launch an investigation into a potential cover up of a sexual assaults perpetrated by Afghani migrants.', 'url': 'https://time.com/4176681/sweden-police-sexual-assault-refugees-migrants-afghans/'},
        ### These are the more tentative links
        'Link 29': {'year': 2017, 'title': 'Police Crackdowns on Immigrants', 'outlet': 'Reuters', 'subtitle': 'Following an April terrorist attack, Swedish police carried out mass investigations of workplace employment records and raids on construction sites, targeting illegal immigrants.', 'url': 'https://www.reuters.com/article/us-sweden-immigration-crackdown/sweden-intensifies-crackdown-on-illegal-immigrants-idUSKBN19Y0G8/'},
        'Link 30': {'year': 2018, 'title': 'Immigrants Perpetrate Most Rapes', 'outlet': 'BBC', 'subtitle': 'Reports show that foreign-born residents commit around 58 percent of rapes, with the number increasing to 80 percent for rapes by strangers.', 'url': 'https://www.bbc.com/news/world-europe-45269764'},
        'Link 31': {'year': 2018, 'title': 'Immigrantion Causing High Unemployment', 'outlet': 'Beaumont Enterprise', 'subtitle': 'Immigrants have a higher unemployment level than native Swedes, driving overall unemployment rates in Sweden to the highest level in the Nordics.', 'url': 'https://www.beaumontenterprise.com/news/article/Unemployment-is-haunting-Sweden-years-after-the-13361549.php'},
        'Link 32': {'year': 2018, 'title': 'Gangs Burn 80 Cars', 'outlet': 'BBC', 'subtitle': 'In coordinated attacks in immigrant neighborhoods, youth gangs set fire to over 80 cars.', 'url': 'https://www.bbc.com/news/world-europe-45181321'},
        'Link 33': {'year': 2018, 'title': 'Anti-Immigration Electoral Gains', 'outlet': 'VOA', 'subtitle': 'The Sweden Democrats, an anti-immigration party, became the third most popular party in parliament after elections.', 'url': 'https://www.voanews.com/a/swedish-anti-immigration-party-gains-popularity/4563667.html'},
        'Link 34': {'year': 2018, 'title': 'Terrorist Sentenced to Life', 'outlet': 'Australian Broadcasting Corporation', 'subtitle': 'Details regarding the sentencing of the 2017 lorry attack perpetrator.', 'url': 'https://www.abc.net.au/news/2018-06-07/stockholm-truck-attack-suspect-gets-life-sentence/9847106'},
        'Link 35': {'year': 2019, 'title': '100 Explosions in Sweden', 'outlet': 'BBC', 'subtitle': 'Sweden is suffering from a sharp increase in intentional explosions and bombings.', 'url': 'https://www.bbc.com/news/world-europe-50339977'},
        'Link 36': {'year': 2019, 'title': 'Increased Border Security', 'outlet': 'Financial Times', 'subtitle': 'An explanation of increased border security measures between Sweden and Denmark following increasing instances of violent crime.', 'url': 'https://www.ft.com/content/9c0d30ea-eb46-11e9-85f4-d00e5018f061'},
        'Link 37': {'year': 2019, 'title': 'Jewish Woman Stabbed in Sweden', 'outlet': 'Jerusalem Post', 'subtitle': 'Details regarding the stabbing of a Jewish woman by a Muslim man in Helsingborg, Sweden.', 'url': 'https://www.jpost.com/diaspora/jewish-woman-stabbed-in-sweden-589669'},
        'Link 38': {'year': 2020, 'title': 'COVID Toll on Immigrants', 'outlet': 'Yahoo News', 'subtitle': 'Report on COVIDs disproportionate effects on immigrant communities in Sweden and Scandinavia.', 'url': 'https://news.yahoo.com/coronavirus-takes-toll-swedens-immigrant-062428162.html?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAFPu_cGZUrebXTMG5UowgIQW0UUvFCuL1gbRJpXjjfN_g-8hSoSZNfbpe0UiQ2a8FaKDdVjUdawiKIqUQetjzYzWgeQerfUHvfM6vtswLFIJ8gc8mEE6Zo85FeA-U2QCvcCe2243n1QAoU6ePsnauMLO1x4Oc9EFGxsoRxf6nhw4'},
        'Link 39': {'year': 2020, 'title': 'New Migration Policies', 'outlet': 'IPS', 'subtitle': 'Explanation of the results of Swedish parliaments months-long negotiations to remake migration policies.', 'url': 'https://www.ips-journal.eu/regions/europe/swedens-never-ending-debate-on-migration-4635/m'},
        'Link 40': {'year': 2020, 'title': 'Worsening Crime in Vulnerable Areas', 'outlet': 'Financial Times', 'subtitle': 'A summary of worsening crimes and gang activity in immigrant populated vulnerable areas.', 'url': 'https://www.ft.com/content/8cfa6212-4270-4962-a200-949a868c7cbe'},
        'Link 41': {'year': 2020, 'title': 'Syrians in Sweden', 'outlet': 'Courthouse News Service', 'subtitle': 'An examination of continuing Syrian migration to Sweden and difficulties of integration in the commnuity.', 'url': 'https://www.courthousenews.com/syrians-still-finding-their-way-in-sweden-five-years-on/'},
        'Link 42': {'year': 2020, 'title': 'Quran Burning Turns Violent', 'outlet': 'i24 News', 'subtitle': 'A summary of events following a Danish politicians public Quran burning in Malmö, Sweden.', 'url': 'https://www.i24news.tv/en/news/international/europe/1598706283-violence-erupts-during-koran-burning-rally-in-sweden'},
        'Link 43': {'year': 2021, 'title': 'Stricter Migration Reforms', 'outlet': 'Forbes', 'subtitle': 'A summary of Swedens new proposed laws on immigration.', 'url': 'https://www.forbes.com/sites/davidnikel/2021/05/13/sweden-pushes-ahead-with-new-immigration-policy/?sh=1916e0659f35'},
        'Link 44': {'year': 2021, 'title': 'Discrimination Against Foreign Doctors', 'outlet': 'Medical XPress', 'subtitle': 'Report on dicrimination against Swedish doctors with foreign backgrounds.', 'url': 'https://medicalxpress.com/news/2021-08-sweden-discrimination-foreign-doctors-widespread.html'},
        'Link 45': {'year': 2021, 'title': 'Stabbing Attack Suspected Terrorism', 'outlet': 'Arab News', 'subtitle': 'Brief description of a stabbing attack by an Afghani in Sweden, suspected to be terrorism related', 'url': 'https://www.arabnews.com/node/1819821/world'},
        'Link 46': {'year': 2021, 'title': 'Increased Crime Blamed on Immigrants', 'outlet': 'Forbes', 'subtitle': 'An investigation into the rise of gang violence and the perceived source--immigrant communities', 'url': 'https://www.forbes.com/sites/lisakim/2021/10/22/swedens-brutal-gang-problem-heres-what-officials-blame-it-on/?sh=936780ba2814'},
        'Link 47': {'year': 2021, 'title': 'Foreign-Born Swedes Disadvataged', 'outlet': 'Reuters', 'subtitle': 'COVIDs economic impacts on foreign-born Swedes in 2021; causes and implications', 'url': 'https://www.reuters.com/article/us-sweden-unemployment-pandemic-idUSKBN2B91MO/'},
        'Link 48': {'year': 2022, 'title': 'Disinformation Among Swedish Muslims', 'outlet': 'France24', 'subtitle': 'A summary of a campaign in Sweden claiming that the government kidnaps Muslim children and places them in Christian households.', 'url': 'https://www.france24.com/en/live-news/20220223-sweden-battles-disinformation-on-kidnappings-of-muslim-children'},
        'Link 49': {'year': 2022, 'title': 'Effects of Swedish Immigration Crisis', 'outlet': 'World News Group', 'subtitle': 'A description of the Swedish immigrant crisis, failed assimilation, and the broader international effects of the crisis .', 'url': 'https://wng.org/opinions/a-swedish-immigration-crisis-is-a-western-crisis-as-well-1657795001'},
        'Link 50': {'year': 2022, 'title': 'Politicians Misconceptions about Segregation', 'outlet': 'The Local--Sweden', 'subtitle': 'A critical analysis of politicians promotion of assimilation and beliefs regarding segragation.', 'url': 'https://www.thelocal.se/20220902/six-things-swedens-politicians-get-wrong-about-segregation'},
        'Link 51': {'year': 2022, 'title': 'Quran Burning Leads to Days of Violence', 'outlet': 'NPR', 'subtitle': 'Report on riots after a Quran burning--police targeted by gangs.', 'url': 'https://www.npr.org/2022/04/18/1093289012/riots-in-sweden'},
        'Link 52': {'year': 2022, 'title': 'Immigrants Turn to Political Action', 'outlet': 'Daily Sabah', 'subtitle': 'Summary of the rise of a new Islamist party gaining traction in immigrant areas.', 'url': 'https://www.dailysabah.com/world/europe/swedens-immigrants-turn-their-backs-on-mainstream-political-parties'},
        'Link 53': {'year': 2023, 'title': 'Swedish PM Summons Army', 'outlet': 'Reuters', 'subtitle': 'Swedish PM Ulf Kristersson summoned the countrys police commissioner and head of the armed forces to discuss gang violence.', 'url': 'https://www.reuters.com/world/europe/sweden-opposition-party-calls-military-tackle-deadly-gang-war-2023-09-28/'},
        'Link 54': {'year': 2023, 'title': 'Borders Reinforced after Quran Burnings', 'outlet': 'Politico EU', 'subtitle': 'Description of political and international ramifications of a series of Quran burnings and subsequent protests.', 'url': 'https://www.politico.eu/article/sweden-quran-burning-embassy-border-control-ulf-kristersson/'},
        'Link 55': {'year': 2023, 'title': 'Non-European Immigrants Targeted by Reforms', 'outlet': 'InfoMigrants', 'subtitle': 'More proposed migration reforms to discourage non-European migrants from coming to Sweden.', 'url': 'https://www.infomigrants.net/en/post/52750/sweden-to-make-it-harder-for-noneuropean-migrants-to-claim-benefits '},
        'Link 56': {'year': 2023, 'title': 'Tighter Conditions for Family Immigration', 'outlet': 'Euractiv', 'subtitle': 'Government coalition proposal to make family immigrantion more difficult.', 'url': 'https://www.euractiv.com/section/politics/news/sweden-to-tighten-conditions-for-family-immigration/'},
        'Link 57': {'year': 2023, 'title': 'Terror Threat Level Raised', 'outlet': 'AP News', 'subtitle': 'Explanation and background on the decision to raise the terror threat level.', 'url': 'https://apnews.com/article/sweden-terror-threat-level-quran-burnings-93df9f95ecae958b64763844d1bc8e4a'},
        'Link 58': {'year': 2010, 'title': 'Anti-Burqa Ad Censored', 'outlet': 'France24', 'subtitle': 'Details the banning of a Sweden Democrats anti-burqa ad because it "incites religious hatred."', 'url': 'https://www.france24.com/en/20100828-swedish-tv-channel-refuses-broadcast-anti-burqa-ad-sweden-democrats-election'},
        'Link 59': {'year': 2010, 'title': 'Sweden Reacts to Muhammad Cartoons', 'outlet': 'NPR', 'subtitle': 'Tells the story of Lars Viks, who drew cartoons of Muhammad, and the response within Sweden.', 'url': 'https://www.npr.org/templates/story/story.php?storyId=124915139'},
        'Link 60': {'year': 2010, 'title': 'Early Sweden Democrats Successes', 'outlet': 'Christian Science Monitor', 'subtitle': 'Summarizes the history of Sweden Democrats and their slow rise to popularity.', 'url': 'https://www.csmonitor.com/World/Europe/2010/1007/Why-Sweden-s-far-right-anti-immigrant-party-made-powerful-gains'},
        'Link 61': {'year': 2011, 'title': 'Denmark Secures Borders', 'outlet': 'Der Spiegel', 'subtitle': 'Description of Denmarks efforts to reduce illegal immigration by increasing customs officials at borders.', 'url': 'https://www.spiegel.de/international/europe/the-world-from-berlin-other-nations-will-follow-denmark-s-example-a-772713.html'},
        'Link 62': {'year': 2011, 'title': 'Suspected Terrorist Arrests', 'outlet': 'Deutsche Welle', 'subtitle': 'Summary of information regarding the arrest of 4 suspsected terrorists in Sweden near the anniversary of 9/11.', 'url': 'https://www.dw.com/en/four-terror-suspects-arrested-in-sweden/a-15379448'},
        'Link 63': {'year': 2012, 'title': 'Demographic Trends and Effects', 'outlet': 'Business Insider', 'subtitle': 'An analysis of the effects of an aging Swedish population and high immigration rates.', 'url': 'https://www.businessinsider.com/sweden-politics-immigration-and-population-ageing-present-policy-challeng-2012-8'},
    }
    
    # Display links based on the selected year
    st.sidebar.markdown(f"## News and Analysis for {selected_year}")

    for link_name, link_info in links_data.items():
        if link_info['year'] == selected_year:
            st.sidebar.markdown(f"### [{link_info['title']}]({link_info['url']})")
            st.sidebar.markdown(f"**Outlet:** {link_info['outlet']}")
            st.sidebar.markdown(f"**Description:** {link_info['subtitle']}")
            st.sidebar.markdown("---")




    ##### MAIN CONTENT #####
    #####
    #####

    ### General Structure ###
    ###

    # Main content in the middle
    st.title('Reconquering Swedenistan')

    # Create tabs
    tab_titles = ['Home', 'Data Exploration', 'Election Results', 'Figures and Tables']
    tabs = st.tabs(tab_titles)

    # Add content to the Data Preprocessing tab
    with tabs[0]:
        st.header('Homepage')
        st.write('***NOTE (12/12/23): This web app is not yet complete, as I am still stress testing and improving various parts of it. It will--in its first official form--be published on Friday, 12/15 along with my research paper. After the initial launch, I will potentially add more detailed election results, a small library of links and summaries of Swedish policies and party platforms, and many more statistics for the data exploration page. Ultimately, I intend for this tool to become an authoritative, comprehensive reference for those hoping to develop a more nuanced, robust view of the immigration issue facing Sweden and, by extension, Europe. Enjoy using the Data Exploration, Election Results, and Figures and Tables tabs for now!***')

        # Spacing
        st.markdown('')
        st.markdown('')
        st.markdown('')

        st.header('Reconquering Swedenistan: An Exploration of Law and Order, Assimilation, and Governmental Sentiment and Policy in Sweden')
        st.write('[INSERT MISSION STATEMENT]')
        st.write('This webapp acts as a companion to [INSERT PDF DOWNLOAD LINK FOR PAPER], published on December 15, 2023 by Ryan Wolff. The paper examines the probable link between assimilation failures, the degredation of law and order, and the political backlash facing immigrants in Sweden, particularly from 2012-2023. This research centers around a sentiment analysis of approximately 17,000 government documents from the Swedish archive [INSERT HYPERLINK]. The code used to scrape, process, and analyze that data can be found at this GitHub repository [INSERT HYPERLINK].')

    # Add content to the Model Training tab
    with tabs[1]:
        st.header('Data Exploration')
        st.write('Explore the data using up to 5 interactive line and scatter plots.')

        # Spacing
        st.markdown('')
        st.markdown('')
        st.markdown('')

        # Extract variables not starting with 'Std.'
        timeline_variables = [var for var in plotting_data.columns if not var.startswith('Std.')]

        # Allow the user to choose x-axis and y-axis variables for each plot
        for i in range(5):  # Creating 5 plots
            # Create two columns for each plot
            col1, col2 = st.columns([2, 8])

            with col1:
                plot_type = st.radio(f"Plot {i + 1} Type:", ('line', 'scatter'))
                y_variable = st.selectbox(f'Y-axis variable for Plot {i + 1}:', timeline_variables)

                # Display variable definition/description with Markdown formatting for the first variable
                variable_description_1 = variable_definitions.loc[variable_definitions['Variable'] == y_variable, 'Definition'].values
                description_text_1 = f"**Definition of {y_variable}:** {variable_description_1[0] if variable_description_1 else 'Not available'}"
                st.markdown(description_text_1, unsafe_allow_html=True)

                # If plot type is 'line', set x_variable to 'Year'
                x_variable = 'Year' if plot_type == 'line' else st.selectbox(f'X-axis variable for Plot {i + 1}:', timeline_variables)

                # Display variable definition/description for the second variable if the plot type is a scatter plot
                if plot_type == 'scatter':
                    variable_description_2 = variable_definitions.loc[variable_definitions['Variable'] == x_variable, 'Definition'].values
                    description_text_2 = f"**Definition of {x_variable}:** {variable_description_2[0] if variable_description_2 else 'Not available'}"
                    st.markdown(description_text_2, unsafe_allow_html=True)

                # Spacing
                st.markdown('')
                st.markdown('')

            with col2:
                # Create a Plotly Express plot based on the user's choice
                fig = None
                if plot_type == 'line':
                    fig = px.line(
                        plotting_data,
                        x=x_variable,
                        y=y_variable,
                        title=f'Plot {i + 1}: {y_variable} Over Time',
                        labels={x_variable: 'Year', y_variable: y_variable},  # Set x-axis label to 'Year'
                        line_shape='linear',
                        hover_data={'Year': '|%B %Y'},
                    )
                elif plot_type == 'scatter':
                    fig = px.scatter(
                        plotting_data,
                        x=x_variable,
                        y=y_variable,
                        title=f'Plot {i + 1}: {y_variable} Over {x_variable}',
                        labels={x_variable: x_variable, y_variable: y_variable},
                        hover_data={'Year': '|%B %Y'},
                    )

                # Display the chart
                st.plotly_chart(fig)

                # Spacing
                st.markdown('')
                st.markdown('')





    # Add content to the Model Evaluation tab
    with tabs[2]:
        st.header('Election Results with Regards to Immigration Policy')
        st.write('Explore recent election results with pie charts.')
        st.write('Friendly parties generally advocate looser immigration laws and increased defenses and/or benefits for immigrants; Hostile parties generally advocate stricter immigration laws.')
        st.markdown('')
        st.markdown('')
        st.markdown('')

        # Dropdown menu for selecting column from a predefined list
        selected_column_options = ['Votes', 'Seats']
        selected_column = st.selectbox('Select Metric:', selected_column_options)

        # Spacing
        st.markdown('')
        st.markdown('')
        st.markdown('')
        

        # Create a pie chart for each year in election_data
        for year in election_data['Year'].unique():
            st.subheader(f'Election Results for {year}')
            year_data = election_data[election_data['Year'] == year]
            
            # Group by 'Class' and the selected column, then sum the values
            pie_data = year_data.groupby(['Class', selected_column]).size().reset_index(name='Count')
            pie_data[selected_column] = pie_data[selected_column].astype(float)  # Ensure the selected column is treated as a numerical type
            pie_data = pie_data.groupby('Class')[selected_column].sum().reset_index()

            # Create a pie chart using Plotly Express with a custom color scale
            fig = px.pie(
                pie_data,
                names='Class',
                values=selected_column,
                title=f'Election Results for {year}',
                hole=0.3,
                color='Class',
                labels={'Class': 'Stance on Immigration'}  # Customize the label
            )

            # Update the legend title
            fig.update_layout(legend_title_text='Stance on Immigration')

            # Display the pie chart
            st.plotly_chart(fig)

    # Add content to the Results Visualization tab
    with tabs[3]:
        st.header('Figures, Tables, and Tests')
        st.write('Explore key figures and statistical tests on this tab.')

        st.header('Order of Contents')
        st.write('1. Summary Table')
        st.write('2. Data on Crime and Demographics')
        st.write('3. Law and Order Metrics')
        st.write('4. Assimilation Metrics')
        st.write('5. Economic Metrics')
        st.write('6. Voter Input')
        st.write('7. Fear-Violence Score')

        # Spacing
        st.markdown("")
        st.markdown("")
        st.markdown("")

        st.header('Summary Table')
        st.image('summary_table.jpg', caption='Grand Summary of Independent and Dependent Variable Tests; Bolding Represents a Statistically-Significant Difference of Means', use_column_width=True)

        # Spacing
        st.markdown("")
        st.markdown("")
        st.markdown("")

        st.header('Data on Crime and Demographics')
        st.image('figure_1.jpg', caption='Figure 1: Maps of Shootings and Demographics Around Stockholm', use_column_width=True)
        st.image('figure_2.jpg', caption='Figure 2: Map of Vulnerable Areas and Demographics Around Stockholm', use_column_width=True)
        st.image('figure_4.jpg', caption='Figure 4: Estimated Proportions of Crime by Immigration Background', use_column_width=True)
        st.markdown("")
        st.markdown("")
        st.markdown("")

        st.header('Law and Order Metrics')
        st.image('figure_5_6.jpg', caption='Figures 5 & 6: T-Tests for Law and Order', use_column_width=True)
        st.image('figure_7.jpg', caption='Figure 7: T-Test for Law and Order', use_column_width=True)
        st.markdown("")
        st.markdown("")
        st.markdown("")

        st.header('Assimilation Metrics')
        st.image('figure_8_9.jpg', caption='Figures 8 & 9: T-Tests for Assimilation', use_column_width=True)
        st.image('figure_10_11.jpg', caption='Figures 10 & 11: T-Tests for Assimilation', use_column_width=True)
        st.image('figure_12.jpg', caption='Figure 12: T-Test for Assimilation', use_column_width=True)
        st.markdown("")
        st.markdown("")
        st.markdown("")

        st.header('Economic Metrics')
        st.image('figure_13_14.jpg', caption='Figures 13 & 14: T-Tests for Economic Control Variables', use_column_width=True)
        st.image('figure_15.jpg', caption='Figure 15: T-Test for Economic Control Variables', use_column_width=True)
        st.markdown("")
        st.markdown("")
        st.markdown("")

        st.header('Voter Input')
        st.image('figure_16_17.jpg', caption='Figures 16 & 17: T-Tests for Immigration and Integration Importance to Voters', use_column_width=True)
        st.image('figure_18_19.jpg', caption='Figures 18 & 19: T-Tests for Law and Order Importance to Voters', use_column_width=True)
        st.markdown("")
        st.markdown("")
        st.markdown("")

        st.header('Fear-Violence Score')
        st.image('results_figure_kennedy.jpg', caption='Figure 20: T-Test for Fear-Violence Scores', use_column_width=True)
        # st.image('figure_20_21.jpg', caption='Figures 20 & 21: T-Tests for Fear-Violence Scores', use_column_width=True)
        # st.image('figure_22.jpg', caption='Figure 22: T-Test for Fear-Violence Scores', use_column_width=True)
        # st.image('figure_23.jpg', caption='Figure 23: T-Test for Fear-Violence Scores', use_column_width=True)
        st.markdown("")
        st.markdown("")
        st.markdown("")

        # st.header('Immigration Reference Frequency')
        # st.image('figure_24_25.jpg', caption='Figures 24 & 25: T-Tests for Proportion of Documents Related to Immigration', use_column_width=True)
        # st.image('figure_26.jpg', caption='Figure 26: T-Test for Proportion of Documents Related to Immigration', use_column_width=True)
        


if __name__ == "__main__":
    main()
