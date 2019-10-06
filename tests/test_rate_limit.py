import os
import unittest

from .config import create_auth
from tweepymashup import API
from tweepmashupy.error import TweepError

testratelimit = 'TEST_RATE_LIMIT' in os.environ


@unittest.skipIf(not testratelimit, "skipping rate limiting test since testratelimit is not specified")
class TweepyRateLimitTests(unittest.TestCase):

    def setUp(self):
        self.api = API(create_auth())
        self.api.retry_count = 2
        self.api.retry_delay = 5
        self.api.retry_errors = {401, 404, 503}
        self.api.wait_on_rate_limit = True

    def testratelimit(self):
        # should cause the api to sleep
        test_user_ids = [123796151, 263168076, 990027860, 901955678, 214630268, 18305040, 36126818, 312483939, 426975332, 469837158, 1104126054, 1342066705, 281632872, 608977002, 242901099, 846643308, 1166401645, 153886833, 95314037, 314458230, 149856382, 287916159, 472506496, 267180736, 251764866, 351035524, 997113991, 445915272, 57335947, 251043981, 95051918, 200761489, 48341139, 972660884, 422330517, 326429297, 864927896, 94183577, 95887514, 220807325, 194330782, 58796741, 1039212709, 1017192614, 625828008, 66539548, 320566383, 309829806, 571383983, 382694863, 439140530, 93977882, 277651636, 19984414, 502004733, 1093673143, 60014776, 469849460, 937107642, 155516395, 1272979644, 617433802, 102212981, 301228831, 805784562, 427799926, 322298054, 162197537, 554001783, 89252046, 536789199, 177807568, 805044434, 495541739, 392904916, 154656981, 291266775, 865454102, 475846642, 56910044, 55834550, 177389790, 339841061, 319614526, 954529597, 595960038, 501301480, 15679722, 938090731, 495829228, 325034224, 1041031410, 18882803, 161080540, 456245496, 636854521, 811974907, 222085372, 222306563, 422846724, 281616645, 223641862, 705786134, 1038901512, 174211339, 426795277, 370259272, 34759594, 366410456, 320577812, 757211413, 483238166, 222624369, 29425605, 456455726, 408723740, 1274608346, 295837985, 273490210, 232497444, 726843685, 465232166, 18850087, 22503721, 259629354, 414250375, 1259941938, 777167150, 1080552157, 1271036282, 1000551816, 109443357, 345781858, 45113654, 406536508, 253801866, 98836799, 395469120, 252920129, 604660035, 69124420, 283459909, 482261729, 377767308, 565240139, 191788429, 102048080, 330054371, 527868245, 177044049, 1250978114, 424042840, 15810905, 389030234, 69324415, 15638877, 159080798, 378708319, 549183840, 1034658145, 629924195, 969130340, 1143593845, 188129639, 535863656, 552452458, 1325277547, 756236624, 48421608, 178495858, 566206836, 378519925, 22678249, 377659768, 102326650, 76783997, 440716178, 49062271, 26296705, 1328036587, 289644932, 305767830, 437305735, 124821901, 591735533, 155140501, 1099612568, 631398810, 469295515, 131350941, 325804447, 529801632, 977197808, 232613818, 614777251, 229261732, 255533478, 256942503, 169583016, 237860252, 29257799, 276668845, 871571886, 398162507, 451954078, 526016951, 285655480, 1281827257, 340042172, 146653629, 61055423, 33407417, 95582321, 237420995, 310960580, 1222064886, 16490950, 60924360, 81928649, 374424010, 45703629, 817455571, 336077264, 400268024, 1203200467, 457105876, 232309205, 45838026, 91972056, 226927065, 82125276, 760131962, 1032274398, 562552291, 155155166, 146464315, 864864355, 128655844, 589747622, 293290470, 192004584, 19100402, 133931498, 19775979, 446374381, 1175241198, 20128240, 332395944, 74575955, 247407092, 427794934, 329823657, 405742072, 497475320, 997384698, 147718652, 757768705, 96757163, 289874437, 29892071, 568541704, 297039276, 356590090, 502055438, 291826323, 238944785, 71483924, 50031538, 863355416, 120273668, 224403994, 14880858, 1241506364, 848962080, 57898416, 599695908, 1222132262, 54045447, 907207212, 851412402, 454418991, 231844616, 618447410, 602997300, 447685173, 19681556, 22233657, 509901138, 184705596, 307624714, 553017923, 1249878596, 33727045, 419873350, 789307489, 287531592, 399163977, 1069425228, 920789582, 136891149, 134857296, 358558478, 436855382, 963011161, 195764827, 548872797, 1058980446, 442376799, 578216544, 527147110, 122077799, 1004773993, 420332138, 514994279, 61530732, 133462802, 19513966, 1286972018, 786121332, 265863798, 221258362, 42656382, 43631231, 198264256, 944382595, 37387030, 260948614, 314406408, 296512982, 92830743, 24519306, 21070476, 454107789, 331006606, 939713168, 256197265, 30065299, 74774188, 1332842606, 289424023, 526992024, 429933209, 116384410, 762143389, 308093598, 421208736, 454943394, 66026267, 158851748, 257550092, 70697073, 903627432, 290669225, 121168557, 92994330, 67642033, 635183794, 499303091, 421205146, 1252648171, 375268025, 16281866, 211960508, 267179466, 129016511, 157172416, 373370004, 167781059, 43624522]
        for user_id in test_user_ids:
            try:
                self.api.user_timeline(user_id=user_id, count=1, include_rts=True)
            except TweepError as e:
                # continue if we're not autherized to access the user's timeline or she doesn't exist anymore
                if e.response is not None and e.response.status in {401, 404}:
                    continue
                raise e

if __name__ == '__main__':
    oauth_consumer_key = os.environ.get('CONSUMER_KEY', '')
    if testratelimit:
        unittest.TextTestRunner().run(unittest.loader.makeSuite(TweepyRateLimitTests))
    else:
        unittest.main()
