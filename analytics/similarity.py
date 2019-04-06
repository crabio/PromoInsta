
import logging
import requests
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# sort can be: 'rank'|'relevance'
def get_similar_hashtag(logger,
                        tags=None,
                        limit=None,
                        sort='relevance'):
        """Generate smart hashtags based on https://displaypurposes.com/"""
        """ranking, banned and spammy tags are filtered out."""

        if tags is None:
            logger.warning('Hash tags is none. Return')
            return

        hashtags = [] # Init list for saving

        for tag in tags:
            query = u'https://d212rkvo8t62el.cloudfront.net/tag/{}'.format(tag)
            req = requests.get(query)
            logger.info(query)

            data = json.loads(req.text)

            if data['tagExists'] is True:
                # sort by sort field
                ordered_tags = sorted(data['results'], key=lambda d: d[sort], reverse=True)
                ordered_limited_tags = (ordered_tags[:limit])
                for item in ordered_limited_tags:
                    # add smart hashtag to like list
                    hashtags.append(item['tag'])

                logger.info(u'[smart hashtag generated: {}]'.format(hashtags))
            else:
                logger.info(u'Too few results for #{} tag'.format(tag))

        # # delete duplicated tags
        # hashtags_list = list(set(self.smart_hashtags))
        # return self

get_similar_hashtag(logger, ['bodyart'])

# text_1 = 'tag1 ' * 10 + 'tag2 ' * 10 + 'tag3 ' * 10
# text_2 = 'tag1 ' * 1 + 'tag2 ' * 1

# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity


# tfidf_vectorizer = TfidfVectorizer()
# tfidf_matrix = tfidf_vectorizer.fit_transform((text_1, text_2))
# result_cos = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
# print(result_cos[0][1])


# from collections import Counter

# list_of_dicts = ([{'dari_ln_tattoo': 0.039689157475414384}, {'captain_partak': 0.004196760745207708}, {'prtck.sketch': 0.043875867537141115}, {'bst_tatts': 0.39542088425685956}, {'bst_tatts': 0.39542088425685956}, {'goran.serb.tattoo': 0.20781620851707877}, {'divotattoo8767': 0.09895367918218712}, {'saint_le': 0.050125113456619866}, {'one.two.tattoo': 0.2947989069878814}, {'tattoo_nhamon': 0.39542088425685956}, {'phoenix_tattooer': 0.13331861125572014}, {'alvol_tattooer': 0.1410849873821999}, {'marinadqtattoo': 0.06268901113765202}, {'marmi_tattoo': 0.16400176808152425}, {'kolshica101': 0.013466644627465987}, {'alexborum': 0.30887602753155774}, {'kolshica101': 0.013466644627465987}, {'tattoo_andrey_': 0.0847029677789122}, {'kolshica101': 0.013466644627465987}, {'hurtlandtattoo': 0.09865114910781725}, {'trendybum_luxtut': 0.02096594924650461}, {'kate_ger_tattoo': 0.22697795150796896}, {'tarasow13tattoo': 0.032514443129057366}, {'kom_tattoo': 0.16972909510027204}, {'morrganttattoo': 0.024693791718287}, {'alexborum': 0.30887602753155774}, {'ilina.tattoo': 0.11262851484258037}, {'mrtsh.tattoo': 0.14568024545487612}, {'annytattoomoscow': 0.053610618817659064}, {'one.two.tattoo': 0.2947989069878814}])

# print({key: val for key, val in list_of_dicts})

# print(a)


######
# import re

# text = '#bodyart #skinartmag #tattoolife #thebesttattooartists #blackandgrey #tattooedlife #inklife #besttattoos #tattooing #inkfreakz #blackandgreytattoo #tattoocommunity #nature_perfection #folkcreative #VisualsOfLife #gearednomad #MoodyGrams #visualambassadors #exklusive_shot #thecreative #peoplescreatives #sombresociety #royalsnappingartists #mskpit #mosquarium #moscowdays #moscowonline #insta_moskva #moscowdaily #bodyart #skinartmag #tattoolife #thebesttattooartists #blackandgrey #tattooedlife #inklife #besttattoos #tattooing #inkfreakz #blackandgreytattoo #tattoocommunity #nature_perfection #folkcreative #VisualsOfLife #gearednomad #MoodyGrams #visualambassadors #exklusive_shot #thecreative #peoplescreatives #sombresociety #royalsnappingartists #mskpit #mosquarium #moscowdays #moscowonline #insta_moskva #moscowdaily #татумосква #inkwell #татувмоскве #татушки #татусалон #tattooart #татуха #tattoolife #татуировщик #татуэскиз #татуировка #татустудия #тату #эскиз #татуировки #татушечка #tattooartist #tattooed #татушка #татуировочка #татумастер #tattoos #tattoo #татухи #bodyart #skinartmag #tattoolife #thebesttattooartists #blackandgrey #tattooedlife #inklife #besttattoos #tattooing #inkfreakz #blackandgreytattoo #tattoocommunity #inkedmag #tattooculture #inkaddict #tattoosociety #inkedlife #supportgoodtattooing #skinart #tattooedpeople #tattoolover #tattoos_alday #meistershots #mskpit #mosquarium #moscowdays #moscowonline #insta_moskva #moscowdaily #bodyart #skinartmag #tattoolife #thebesttattooartists #blackandgrey #tattooedlife #inklife #besttattoos #tattooing #inkfreakz #blackandgreytattoo #tattoocommunity #inkedmag #tattooculture #inkaddict #tattoosociety #inkedlife #supportgoodtattooing #skinart #tattooedpeople #tattoolover #tattoos_alday #meistershots #mskpit #mosquarium #moscowdays #moscowonline #insta_moskva #moscowdaily #focalmarked'

# text_extended = ''

# text_list = re.findall('#(\w+)', text)

# text_distinct_list = list(set(text_list))

# print(' '.join(text_distinct_list))

# extended_text = '#thecoolmagazine #mobilefolk #folkscenery #byfolk #superhubs #judeallen1 #folkmagazine #vscogood_ #hypekillsmag #chasingemotions #customtattoo #tattoostyle #folkvibe #1stinstinct #expofilm #uktta #ntgallery #neotradsub #thebestspaintattooartists #electricink #supportgoodtattooers #worldfamousink #inkaddicts #tattrx #tattoosnob #tattooculturemagazine #fusionink #tattooedwomen #tatouage #tattooidea #tatuajes #tattoogirls #msk_moscow #kudago #москвариум #i_love_msk #кругсвета #ялюблюмоскву #nature_brilliance #nature_sultans #nature_shooters #allnatureshots #nature_wizards #naturehippys #bestnatureshot #natureaddict #naturelover #naturegram #natureza #instanature #natureshots #natureporn #nature_seekers #bestnatureshots #worldcaptures #instanaturefriends_ #naturelover_gr #photoarena_nature #sunset_madness #natureonly #earth_deluxe #tattoomodel #visualmobs #такяснимаю #streetdreams #streethype #seemycity #guardiancities #analoguepeople #heyfsc #filmisalive #theanalogueproject #buyfilmnotmegapixels #filmcommunity #analogphotography #staybrokeshootfilm #believeinfilm #tangledinfilm #ishootfilm #urbex #inkfreakz #instagramrussia #instarussia #инстаграмнедели #russia_ww #vscorussia #natgeoru #mextures #handtattoo #chesttattoo #coverup #bodypaint #m3xtures #thedarkpr0ject #sombrexplore #romantic_darkness #mode_emotive #sombrebeings #rsa_dark #themysterypr0ject #pr0ject_soul #fa_fadeaway #jj_sombre #gloomgrabber #humanedge #artistry_flair #kings_abandoned #sombrebw #fiftyshades_of_darkness #wonderland_arts #feedbacknation #tattoogirl #tattoodo #equilattera #toptattooartist #inkjunkeyz #the_inkmasters #tattoolifemagazine #tattooworkers #tattooartistmagazine #tatu #tattoorevuemagazine #skinartmagazine #igmoscow #mskfoto #hbouthere #taot #inkedmag #amazingink #for_moscow #moscowbeauty #kudagomsk #onedaymoscow #mskphotoday #photorussia #msk_town #vscomoscow #moscow_gram #inkmaster #vscocamrussia #инстаграм_порусски #татувмоскве #tattooistartmagazine #tattooistartmag #thebesttattooartists #tattoo_art_worldwide #heart_imprint #bevisuallyinspired #tattoosofinstagram #thecreative #inksav #tattoo_artwork #фотодляроссии #inkig #savemyink #tattooing #tetovani #tater #trasher #индивидуальность #linework #trash #moscowcity #superbtattoos #portraitpage #urbangathering #freshlyinked #tat #татуэскиз #piercings #girlswithink #guyswithtattoos #татуировка #folkgood #folkcreative #symmetricalmonsters #bnginksociety #msk #tattoooftheday #all_about_moscow #rus_places #lovelyrussia #blackandgreytattoo #postthepeople #finditliveit #makeportraits #welltravelled #vscogrid #communityfirst #wanderfolk #chasinglight #lookslikefilm #featuremeofh #welltraveled #streetmobs #ilovemoscow #stayandwander #i_moskva #insta_moskva #moscowdays #moscowonline #mskpit #mosquarium #vzcomood #tattooedpeople #supportgoodtattooing #tattoocommunity #tattoolover #estheticlabel #tattooer #rsa_nature #rsa_rural #fiftyshades_of_nature #gottalove_a_ #tattooink #blackandgreytattoos #moscowdaily #msk_gram #моямосква #realistictattoo #realismtattoo #portraittattoo #realism #blacktattoo #meistershots #urbanandstreet #createexploretakeover #killeverygram #ftwotw #bleachmyfilm #featuremeinstagood #huntgram #тату #inkaddict #tattooedcommunity #tattooculture #tattoosalday #support_good_tattooing #sharon_alday #besttattoos #instatattoo #inkedup #tattooart #imaginatones #tats #yngkillers #gearednomad #tattooflash #skinartmag #tattoist #sleevetattoo #tattoolove #inklife #татусалон #татумосква #татумастер #inkedlife #skinart #aov #tattoolife #traditionaltattoo #weekly_feature #tattoosociety #master_shots #global_hotshotz #special_shots #hot_shotz #canon_photos #ig_exquisite #phototag_it #tattoos_alday #tattoorevuemag #tattooartist #shotzdelight #bodyart #inkedgirls #tatted #sombrescapes #sombresociety #pr0ject_uno #wowmoscow #instamoscow #rsa_naturepics #mist_bestshots #soft_vision #fingerprintofgod #rsa_mextures #global_ladies #inkedbabes #inkedandsexy #inkedchicks #tattooedlife #tattooshop #visualambassadors #татустудия #inkedgirl #tattoos #татухи #татушка #tattooed #landscape_captures #landscape_lovers #visualarchitects #tattedup #onlinemoscow #tattooedgirls #usaprimeshot #татуха #татуировки #visualsgang #instagoodmyphoto #ig_color #tatts #citykillerz #streetshared #streetmagazine #mg5k #tattoodesign #inmsk #loves_moscow #moscow_ig #moscow_city_photo #ilovemsk #awesome_russia #moscowphoto #tattooist #mkexplore #hsdailyfeature #ink #russia_fotolovers #loves_russia #loves_united_russia #rsa_streetview #inkstagram #inked #murderdotcom #urbanaisle #aov5k #houseoftones #compositionkillerz #acreativevisual #all2epic #girlswithtattoos #createandcapture #agameof10k #streets_vision #letsgosomewhere #socality #freedomthinkers #streetactivity #streetmeetina #twgrammers #aestheticshot #loaded_lenses #gramslayers #moscow_life #tatuagem #instamagazine_ #uncalculated #blackandgrey #tattooinrussia #blacktattooart #btattooing #tatoo #streetcollectors #tattoocollection #tattooaddicts #tattooartwork #tatuaggio #topclasstattooing #theoutbound #exploremore #roamtheplanet #superb_tattoos #cooltattoos #tattooed_body_art #amazingtattoos #inkjecta #stencilstuff #sullenclothing #tatuaje #infamous_family #rsa_ladies #tv_living #tv_depthoffield #rsa_vsco #tv_pointofview #click_vision #tv_allnature #tv_community #tv_landscapes #tv_aqua #tattooaddict #blackwork #dotwork #bng #rosetattoo #silverbackink #blackworkers #moscowlife #moscowmoscow #moscowmule #moscowneversleeps #mymoscow #москваялюблютебя #moscowregion #moscowgirl #moscowviews #москвасейчас #москвасити #москва2016 #moscowriver #москварека #moscowraceway #colortattoo #тело #мехенди #хна #mehendi #менди #грудь #биотату #блондинка #соски #ванна #зеркало #брюнетка #сиськи #разврат #welivetoexplore #awesome_earthpix #peoplescreative #beautifulplaces #EarthVisuals #tattoostudio #эскиз #набросок #скетч #рисунок #арт'


