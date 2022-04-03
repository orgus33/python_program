import random
from termcolor import colored


class color:
    BOLD = "\033[1m"
    END = "\033[0m"


print("\n" * 100)
print("Quel temps voulez-vous réviser ?")
print("1 - Présent de l'indicatif")
print("2 - Présent du subjonctif")
print("3 - Imparfait de l'indicatif")
print("4 - Passé simple")
print("5 - Imparfait du subjonctif")
print("6 - Futur")
print("7 - Conditionnelle")
print("8 - Gérondif")

temps = int(input("Temps: "))
print(""), print(
    "Si vous voulez quitter à tout moment, veuillez marquer",
    colored("quit", "yellow"),
    "et vous serez automatiquement redirigé vers la fin.",
), print(""), print("")

if temps == 1:
    marcher = [("marcher", "andar"), ("ando", "andas",
                                      "anda", "andamos", "andáis", "andan")]
    dire = [("dire", "decir"), ("digo", "dices",
                                "dice", "decimos", "decis", "dicen")]
    déduire = [
        ("déduire", "deducir"),
        ("deduzco", "deduces", "deduce", "deducimos", "deducís", "deducen"),
    ]
    connaître = [
        ("connaître", "conocer"),
        ("conozco", "conoces", "conoce", "conocemos", "conocéis", "conocen"),
    ]
    raconter = [
        ("raconter", "contar"),
        ("cuento", "cuentas", "cuenta", "contamos", "contáis", "cuentan"),
    ]
    parler = [("parler", "hablar"), ("hablo", "hablas",
                                     "habla", "hablamos", "habláis", "hablan")]
    demander = [("demander", "pedir"), ("pido", "pides",
                                        "pide", "pedemos", "pedis", "piden")]
    venir = [("venir", "venir"), ("vengo", "vienes",
                                  "viene", "venimos", "venís", "vienen")]
    donner = [("donner", "dar"), ("doy", "das", "da", "damos", "dais", "dan")]
    avoir_aux = [("avoir (auxiliaire)", "haber"),
                 ("he", "has", "ha", "hemos", "habéis", "han")]
    tomber = [("tomber", "caer"), ("caigo", "caes",
                                   "cae", "caemos", "caéis", "caen")]
    dormir = [
        ("dormir", "dormir"),
        ("duermo", "duermes", "duerme", "dormimos", "dormís", "duermen"),
    ]
    faire = [("faire", "hacer"), ("hago", "haces",
                                  "hace", "hacemos", "hacéis", "hacen")]
    avoir_posseder = [
        ("avoir / posseder", "Tener"),
        ("tengo", "tienes", "tiene", "tenemos", "tenéis", "tienen"),
    ]
    être_situation = [
        ("être (se situer)", "Estar"),
        ("estoy", "estás", "está", "estamos", "estáis", "están"),
    ]
    être = [("être (être)", "Ser"),
            ("soy", "eres", "es", "somos", "sois", "son")]
    manger = [("manger", "comer"), ("como", "comes",
                                    "come", "comemos", "coméis", "comen")]
    entendre = [("entendre", "oir"), ("oigo", "oyes",
                                      "oye", "oímos", "oís", "oyen")]
    sentir_ressentir = [
        ("sentir/ressentir", "sentir"),
        ("siento", "sientes", "siente", "sentimos", "sentis", "sienten"),
    ]
    mettre = [("mettre", "poner"), ("pongo", "pones",
                                    "pone", "ponemos", "ponéis", "ponen")]
    vouloir_aimer = [
        ("vouloir / aimer", "querer"),
        ("quiero", "quieres", "quiere", "queremos", "queréis", "quieren"),
    ]
    apporter = [("apporter", "traer"), ("traigo", "traes",
                                        "trae", "traemos", "traéis", "traen")]
    pouvoir = [("pouvoir", "poder"), ("puedo", "puedes",
                                      "puede", "podemos", "podéis", "pueden")]
    vivre = [("vivre", "vivir"), ("vivo", "vives",
                                  "vive", "vivimos", "vivis", "viven")]
    sortir = [("sortir", "salir"), ("salgo", "sales",
                                    "sale", "salimos", "salis", "salen")]
    penser = [
        ("penser", "pensar"),
        ("pienso", "piensas", "piensa", "pensamos", "pensáis", "piensan"),
    ]
    aller = [("aller", "ir"), ("voy", "vas", "va", "vamos", "vais", "van")]
    savoir = [("savoir", "saber"), ("sé", "sabes",
                                    "sabe", "sabemos", "sabéis", "saben")]
    voir = [("ver", "voir"), ("veo", "ves", "ve", "vemos", "veis", "ven")]
    list_verbe = (
        marcher,
        dire,
        déduire,
        connaître,
        raconter,
        parler,
        demander,
        venir,
        donner,
        avoir_aux,
        tomber,
        dormir,
        faire,
        avoir_posseder,
        être_situation,
        être,
        manger,
        entendre,
        sentir_ressentir,
        mettre,
        vouloir_aimer,
        apporter,
        pouvoir,
        vivre,
        sortir,
        penser,
        aller,
        savoir,
        voir,
    )
    list_place = ("Yo", "tu", "el, ella", "nosotros",
                  "vosotros", "ellos, ellas")

elif temps == 2:
    parler = [("parler", "hablar"), ("hable", "hables",
                                     "hable", "hablemos", "habléis", "hablen")]
    manger = [("manger", "Comer"), ("coma", "comas",
                                    "coma", "comamos", "comáis", "coman")]
    vivre = [("vivre", "vivir"), ("viva", "vivas",
                                  "viva", "vivamos", "viváis", "vivan")]
    marcher = [("marcher", "andar"), ("ande", "andes",
                                      "ande", "andemos", "andéis", "anden")]
    tomber = [("tomber", "caer"), ("caiga", "caigas",
                                   "caiga", "caigamos", "caigáis", "caigan")]
    donner = [("donner", "dar"), ("dé", "des", "dé", "demos", "deis", "den")]
    dire = [("dire", "decir"), ("diga", "digas",
                                "diga", "digamos", "digáis", "digan")]
    être_situation = [
        ("être (se situer)", "Estar"),
        ("esté", "estés", "este", "estemos", "estéis", "estén"),
    ]
    avoir_aux = [
        ("avoir (auxiliaire)", "haber"),
        ("haya", "hayas", "haya", "hayamos", "hayáis", "hayan"),
    ]
    faire = [("faire", "hacer"), ("haga", "hagas",
                                  "haga", "hagamos", "hagáis", "hagan")]
    aller = [("aller", "ir"), ("vaya", "vayas",
                               "vaya", "vayamos", "vayáis", "vayan")]
    entendre = [("entendre", "oir"), ("oiga", "oigas",
                                      "oiga", "oigamos", "oigáis", "oyan")]
    pouvoir = [("pouvoir", "poder"), ("pueda", "puedas",
                                      "pueda", "podamos", "podáis", "puedan")]
    mettre = [("mettre", "poner"), ("ponga", "pongas",
                                    "ponga", "pongamos", "pongáis", "pongan")]
    vouloir_aimer = [
        ("vouloir_aimer", "querer"),
        ("quiera", "quieras", "quiera", "queramos", "queráis", "quieran"),
    ]
    savoir = [("savoir", "saber"), ("sepa", "sepas",
                                    "sepa", "sepamos", "sepáis", "sepan")]
    sortir = [("sortir", "Salir"), ("salga", "salgas",
                                    "salga", "salgamos", "salgáis", "salgan")]
    être = [("être (être)", "Ser"), ("sea", "seas",
                                     "sea", "seamos", "seáis", "sean")]
    avoir_posseder = [
        ("avoir_posseder", "Tener"),
        ("tenga", "tengas", "tenga", "tengamos", "tengáis", "tengan"),
    ]
    apporter = [
        ("apporter", "traer"),
        ("traiga", "traigas", "traiga", "traigamos", "traigáis", "traigan"),
    ]
    venir = [("venir", "venir"), ("venga", "vengas",
                                  "venga", "vengamos", "vengáis", "vengan")]
    voir = [("ver", "voir"), ("vea", "veas", "vea", "veamos", "veáis", "vean")]
    penser = [
        ("penser", "pensar"),
        ("piense", "pienses", "piense", "pensemos", "penséis", "piensen"),
    ]
    raconter = [
        ("raconter", "contar"),
        ("cuente", "cuentes", "cuente", "contemos", "contéis", "cuenten"),
    ]
    demander = [("demander", "pedir"), ("pida", "pidas",
                                        "pida", "pidamos", "pidáis", "pidan")]
    sentir_ressentir = [
        ("sentir/ressentir", "Sentir"),
        ("sienta", "sientas", "sienta", "sintamos", "sintáis", "sientan"),
    ]
    dormir = [
        ("dormir", "dormir"),
        ("duerma", "duermas", "duerma", "durmamos", "durmáis", "duerman"),
    ]
    connaître = [
        ("connaître", "conocer"),
        ("conozca", "conozcas", "conozca", "conozcamos", "conozcáis", "conozcan"),
    ]
    déduire = [
        ("déduire", "deducir"),
        ("deduzca", "deduzcas", "deduzca", "deduzcamos", "deduzcáis", "deduzcan"),
    ]

    list_verbe = (
        marcher,
        dire,
        déduire,
        connaître,
        raconter,
        parler,
        demander,
        venir,
        donner,
        avoir_aux,
        tomber,
        dormir,
        faire,
        avoir_posseder,
        être_situation,
        être,
        manger,
        entendre,
        sentir_ressentir,
        mettre,
        vouloir_aimer,
        apporter,
        pouvoir,
        vivre,
        sortir,
        penser,
        aller,
        savoir,
        voir,
    )
    list_place = ("Yo", "tu", "el, ella", "nosotros",
                  "vosotros", "ellos, ellas")

elif temps == 4:
    parler = [
        ("parler", "hablar"),
        ("hablé", "hablaste", "habló", "hablamos", "hablasteis", "hablaron"),
    ]
    marcher = [
        ("marcher", "andar"),
        ("anduve", "anduviste", "anduvo", "anduvimos", "anduvisteis", "anduvieron"),
    ]
    dire = [("dire", "decir"), ("dije", "dijiste",
                                "dijo", "dijimos", "dijisteis", "dijeron")]
    donner = [("donner", "dar"), ("di", "diste",
                                  "dio", "dimos", "disteis", "dieron")]
    être_situation = [
        ("être (se situer)", "Estar"),
        ("estuve", "estuviste", "estuvo", "estuvimos", "estuvisteis", "estuvieron"),
    ]
    faire = [("faire", "hacer"), ("hice", "hiciste",
                                  "hizo", "hicimos", "hicisteis", "hicieron")]
    aller = [("aller", "ir"), ("fui", "fuiste",
                               "fue", "fuimos", "fuisteis", "fueron")]
    manger = [("manger", "Comer"), ("comí", "comiste",
                                    "comió", "comimos", "comisteis", "comieron")]
    vivre = [("vivre", "vivir"), ("vivi", "viviste",
                                  "vivió", "vivimos", "vivisteis", "vivieron")]
    tomber = [("tomber", "caer"), ("caí", "caiste",
                                   "cayó", "caímos", "caísteis", "cayeron")]
    avoir_aux = [
        ("avoir (auxiliaire)", "haber"),
        ("hube", "hubiste", "hubo", "hubimos", "hubisteis", "hubieron"),
    ]
    entendre = [("entendre", "oir"), ("oí", "oíste",
                                      "oyó", "oímos", "oísteis", "oyeron")]
    pouvoir = [
        ("pouvoir", "poder"),
        ("pude", "pudiste", "pudo", "pudimos", "pudisteis", "pudieron"),
    ]
    mettre = [("mettre", "poner"), ("puse", "pusiste",
                                    "puso", "pusimos", "pusisteis", "pusieron")]
    vouloir_aimer = [
        ("vouloir_aimer", "querer"),
        ("quise", "quisiste", "quiso", "quisimos", "quisisteis", "quisieron"),
    ]
    savoir = [("savoir", "saber"), ("supe", "supiste",
                                    "supo", "supimos", "supisteis", "supieron")]
    sortir = [("sortir", "Salir"), ("salí", "saliste",
                                    "salió", "salimos", "salisteis", "salieron")]
    être = [("être (être)", "Ser"), ("fui", "fuiste",
                                     "fue", "fuimos", "fuisteis", "fueron")]
    avoir_posseder = [
        ("avoir_posseder", "Tener"),
        ("tuve", "tuviste", "tuvo", "tuvimos", "tuvisteis", "tuvieron"),
    ]
    apporter = [
        ("apporter", "traer"),
        ("traje", "trajiste", "trajo", "trajimos", "trajisteis", "trajeron"),
    ]
    venir = [("venir", "venir"), ("vine", "viniste",
                                  "vino", "vinimos", "vinisteis", "vinieron")]
    voir = [("voir", "ver"), ("vi", "viste",
                              "vio", "vimos", "visteis", "vieron")]
    penser = [
        ("penser", "pensar"),
        ("pensé", "pensaste", "pensó", "pensamos", "pensasteis", "pensaron"),
    ]
    raconter = [
        ("raconter", "contar"),
        ("conté", "contaste", "contó", "contamos", "contasteis", "contaron"),
    ]
    demander = [
        ("demander", "pedir"),
        ("pedí", "pediste", "pidió", "pedimos", "pedisteis", "pidieron"),
    ]
    sentir_ressentir = [
        ("sentir/ressentir", "Sentir"),
        ("sentí", "sentiste", "sintió", "sentimos", "sentisteis", "sintieron"),
    ]
    dormir = [
        ("dormir", "dormir"),
        ("dormí", "dormiste", "durmió", "dormimos", "dormisteis", "durmieron"),
    ]
    connaître = [
        ("connaître", "conocer"),
        ("conocí", "conociste", "conoció", "conocimos", "conocisteis", "conocieron"),
    ]
    déduire = [
        ("déduire", "deducir"),
        ("deduje", "dedujiste", "dedujo", "dedujimos", "dedujisteis", "dedujeron"),
    ]

    list_verbe = (
        marcher,
        dire,
        déduire,
        connaître,
        raconter,
        parler,
        demander,
        venir,
        donner,
        avoir_aux,
        tomber,
        dormir,
        faire,
        avoir_posseder,
        être_situation,
        être,
        manger,
        entendre,
        sentir_ressentir,
        mettre,
        vouloir_aimer,
        apporter,
        pouvoir,
        vivre,
        sortir,
        penser,
        aller,
        savoir,
        voir,
    )
    list_place = ("Yo", "tu", "el, ella", "nosotros",
                  "vosotros", "ellos, ellas")

elif temps == 3:
    parler = [
        ("parler", "hablar"),
        ("hablaba", "hablabas", "hablaba", "hablábamos", "hablabais", "hablaban"),
    ]
    marcher = [
        ("marcher", "andar"),
        ("andaba", "andabas", "andaba", "andábamos", "andabais", "andaban"),
    ]
    tomber = [("tomber", "caer"), ("caía", "caías",
                                   "caía", "caíamos", "caíais", "caían")]
    dire = [("dire", "decir"), ("decía", "decías",
                                "decía", "decíamos", "decíais", "decían")]
    donner = [("donner", "dar"), ("daba", "dabas",
                                  "daba", "dábamos", "dabais", "daban")]
    être_situation = [
        ("être (se situer)", "Estar"),
        ("estaba", "estabas", "estaba", "estábamos", "estabais", "estaban"),
    ]
    faire = [("faire", "hacer"), ("hacía", "hacías",
                                  "hacía", "hacíamos", "hacíais", "hacían")]
    aller = [("aller", "ir"), ("iba", "ibas",
                               "iba", "íbamos", "ibais", "iban")]
    manger = [("manger", "Comer"), ("comía", "comías",
                                    "comía", "comíamos", "comíais", "comían")]
    vivre = [("vivre", "vivir"), ("vivía", "vivías",
                                  "vivía", "vivíamos", "vivíais", "vivían")]
    avoir_aux = [
        ("avoir (auxiliaire)", "haber"),
        ("había", "habías", "había", "habíamos", "habíais", "habían"),
    ]
    entendre = [("entendre", "oir"), ("oía", "oías",
                                      "oía", "oíamos", "oíais", "oían")]
    pouvoir = [("pouvoir", "poder"), ("podía", "podías",
                                      "podía", "podíamos", "podíais", "podían")]
    mettre = [("mettre", "poner"), ("ponía", "ponías",
                                    "ponía", "poníamos", "poníais", "ponían")]
    vouloir_aimer = [
        ("vouloir_aimer", "querer"),
        ("quería", "querías", "quería", "queríamos", "queríais", "querían"),
    ]
    savoir = [("savoir", "saber"), ("sabía", "sabías",
                                    "sabía", "sabíamos", "sabíais", "sabían")]
    sortir = [("sortir", "Salir"), ("salía", "salías",
                                    "salía", "salíamos", "salíais", "salían")]
    être = [("être (être)", "Ser"), ("era", "eras",
                                     "era", "éramos", "erais", "eran")]
    avoir_posseder = [
        ("avoir_posseder", "Tener"),
        ("tenía", "tenías", "tenía", "teníamos", "teníais", "tenían"),
    ]
    apporter = [
        ("apporter", "traer"),
        ("traía", "traías", "traía", "traíamos", "traíais", "traían"),
    ]
    venir = [("venir", "venir"), ("venía", "venías",
                                  "venía", "veníamos", "veníais", "venían")]
    voir = [("voir", "ver"), ("veía", "veías",
                              "veía", "veíamos", "veíais", "veían")]
    penser = [
        ("penser", "pensar"),
        ("pensaba", "pensabas", "pensaba", "pensábamos", "pensabais", "pensaban"),
    ]
    raconter = [
        ("raconter", "contar"),
        ("contaba", "contabas", "contaba", "contábamos", "contabais", "contaban"),
    ]
    demander = [
        ("demander", "pedir"),
        ("pedía", "pedías", "pedía", "pedíamos", "pedíais", "pedían"),
    ]
    sentir_ressentir = [
        ("sentir/ressentir", "Sentir"),
        ("sentía", "sentías", "sentía", "sentíamos", "sentíais", "sentían"),
    ]
    dormir = [
        ("dormir", "dormir"),
        ("dormía", "dormías", "dormía", "dormíamos", "dormíais", "dormían"),
    ]
    connaître = [
        ("connaître", "conocer"),
        ("conocía", "conocías", "conocía", "conocíamos", "conocíais", "conocían"),
    ]
    déduire = [
        ("déduire", "deducir"),
        ("deducía", "deducías", "deducía", "deducíamos", "deducíais", "deducían"),
    ]

    list_verbe = (
        marcher,
        dire,
        déduire,
        connaître,
        raconter,
        parler,
        demander,
        venir,
        donner,
        avoir_aux,
        tomber,
        dormir,
        faire,
        avoir_posseder,
        être_situation,
        être,
        manger,
        entendre,
        sentir_ressentir,
        mettre,
        vouloir_aimer,
        apporter,
        pouvoir,
        vivre,
        sortir,
        penser,
        aller,
        savoir,
        voir,
    )
    list_place = ("Yo", "tu", "el, ella", "nosotros",
                  "vosotros", "ellos, ellas")

elif temps == 5:
    parler = [
        ("parler", "hablar"),
        ("hablara", "hablaras", "hablara", "habláramos", "hablarais", "hablaran"),
    ]
    marcher = [
        ("marcher", "andar"),
        ("anduviera", "anduvieras", "anduviera",
         "anduviéramos", "anduvierais", "anduvieran"),
    ]
    donner = [("donner", "dar"), ("diera", "dieras",
                                  "diera", "diéramos", "dierais", "dieran")]

    dire = [("dire", "decir"), ("dijera", "dijeras",
                                "dijera", "dijéramos", "dijerais", "dijeran")]
    être_situation = [
        ("être (se situer)", "Estar"),
        ("estuviera", "estuvieras", "estuviera",
         "estuviéramos", "estuvierais", "estuvieran"),
    ]
    faire = [
        ("faire", "hacer"),
        ("hiciera", "hicieras", "hiciera", "hiciéramos", "hicierais", "hicieran"),
    ]
    aller = [("aller", "ir"), ("fuera", "fueras",
                               "fuera", "fuéramos", "fuerais", "fueran")]
    manger = [
        ("manger", "Comer"),
        ("comiera", "comieras", "comiera", "comiéramos", "comierais", "comieran"),
    ]
    vivre = [
        ("vivre", "vivir"),
        ("viviera", "vivieras", "viviera", "viviéramos", "vivierais", "vivieran"),
    ]
    tomber = [
        ("tomber", "caer"),
        ("cayera", "cayeras", "cayera", "cayéramos", "cayerais", "cayeran"),
    ]
    avoir_aux = [
        ("avoir (auxiliaire)", "haber"),
        ("hubiera", "hubieras", "hubiera", "hubiéramos", "hubierais", "hubieran"),
    ]
    entendre = [("entendre", "oir"), ("oyera", "oyeras",
                                      "oyera", "oyéramos", "oyerais", "oyeran")]
    pouvoir = [
        ("pouvoir", "poder"),
        ("pudiera", "pudieras", "pudiera", "pudiéramos", "pudierais", "pudieran"),
    ]
    mettre = [
        ("mettre", "poner"),
        ("pusiera", "pusieras", "pusiera", "pusiéramos", "pusierais", "pusieran"),
    ]
    vouloir_aimer = [
        ("vouloir_aimer", "querer"),
        ("quisiera", "quisieras", "quisiera",
         "quisiéramos", "quisierais", "quisieran"),
    ]
    savoir = [
        ("savoir", "saber"),
        ("supiera", "supieras", "supiera", "supiéramos", "supierais", "supieran"),
    ]
    sortir = [
        ("sortir", "Salir"),
        ("saliera", "salieras", "saliera", "saliéramos", "salierais", "salieran"),
    ]
    être = [("être (être)", "Ser"), ("fuera", "fueras",
                                     "fuera", "fuéramos", "fuerais", "fueran")]

    avoir_posseder = [
        ("avoir_posseder", "Tener"),
        ("tuviera", "tuvieras", "tuviera", "tuviéramos", "tuvierais", "tuvieran"),
    ]
    apporter = [
        ("apporter", "traer"),
        ("trajera", "trajeras", "trajera", "trajéramos", "trajerais", "trajeran"),
    ]
    venir = [
        ("venir", "venir"),
        ("viniera", "vinieras", "viniera", "viniéramos", "vinierais", "vinieran"),
    ]
    voir = [("voir", "ver"), ("viera", "vieras",
                              "viera", "viéramos", "vierais", "vieran")]
    penser = [
        ("penser", "pensar"),
        ("pensara", "pensaras", "pensara", "pensáramos", "pensarais", "pensaran"),
    ]
    raconter = [
        ("raconter", "contar"),
        ("contara", "contaras", "contara", "contáramos", "contarais", "contaran"),
    ]

    demander = [
        ("demander", "pedir"),
        ("pidiera", "pidieras", "pidiera", "pidiéramos", "pidierais", "pidieran"),
    ]
    sentir_ressentir = [
        ("sentir/ressentir", "Sentir"),
        ("sintiera", "sintieras", "sintiera",
         "sintiéramos", "sintierais", "sintieran"),
    ]
    dormir = [
        ("dormir", "dormir"),
        ("durmiera", "durmieras", "durmiera",
         "durmiéramos", "durmierais", "durmieran"),
    ]
    connaître = [
        ("connaître", "conocer"),
        ("conociera", "conocieras", "conociera",
         "conociéramos", "conocierais", "conocieran"),
    ]
    déduire = [
        ("déduire", "deducir"),
        ("dedujera", "dedujeras", "dedujera",
         "dedujéramos", "dedujerais", "dedujeran"),
    ]

    list_verbe = (
        marcher,
        dire,
        déduire,
        connaître,
        raconter,
        parler,
        demander,
        venir,
        donner,
        avoir_aux,
        tomber,
        dormir,
        faire,
        avoir_posseder,
        être_situation,
        être,
        manger,
        entendre,
        sentir_ressentir,
        mettre,
        vouloir_aimer,
        apporter,
        pouvoir,
        vivre,
        sortir,
        penser,
        aller,
        savoir,
        voir,
    )
    list_place = ("Yo", "tu", "el, ella", "nosotros",
                  "vosotros", "ellos, ellas")

elif temps == 6:
    parler = [
        ("parler", "hablar"),
        ("hablaré", "hablarás", "hablará", "hablaremos", "hablaréis", "hablaran"),
    ]
    marcher = [
        ("marcher", "andar"),
        ("andaré", "andarás", "andará", "andaremos", "andaréis", "andaran"),
    ]
    donner = [("donner", "dar"), ("daré", "darás",
                                  "dará", "daremos", "daréis", "darán")]

    dire = [("dire", "decir"), ("diré", "dirás",
                                "dirá", "diremos", "diréis", "dirán")]
    être_situation = [
        ("être (se situer)", "Estar"),
        ("estaré", "estarás", "estará", "estaremos", "estaréis", "estarán"),
    ]
    faire = [("faire", "hacer"), ("haré", "harás",
                                  "hará", "haremos", "haréis", "harán")]
    aller = [("aller", "ir"), ("iré", "irás",
                               "irá", "iremos", "iréis", "irán")]
    manger = [
        ("manger", "Comer"),
        ("comeré", "comerás", "comerá", "comeremos", "comeréis", "comerán"),
    ]
    vivre = [
        ("vivre", "vivir"),
        ("viviré", "vivirás", "vivirá", "viviremos", "viviréis", "vivirán"),
    ]
    tomber = [("tomber", "caer"), ("caeré", "caerás",
                                   "caerá", "caeremos", "caeréis", "caerán")]
    avoir_aux = [
        ("avoir (auxiliaire)", "haber"),
        ("habré", "habrás", "habrá", "habremos", "habréis", "habrán"),
    ]
    entendre = [("entendre", "oir"), ("oiré", "oirás",
                                      "oirá", "oiremos", "oiréis", "oirán")]
    pouvoir = [("pouvoir", "poder"), ("podré", "podrás",
                                      "podrá", "podremos", "podréis", "podrán")]
    mettre = [
        ("mettre", "poner"),
        ("pondré", "pondrás", "pondrá", "pondremos", "pondréis", "pondrán"),
    ]
    vouloir_aimer = [
        ("vouloir_aimer", "querer"),
        ("querré", "querrás", "querrá", "querremos", "querréis", "querrán"),
    ]
    savoir = [("savoir", "saber"), ("sabré", "sabrás",
                                    "sabrá", "sabremos", "sabréis", "sabrán")]
    sortir = [
        ("sortir", "Salir"),
        ("saldré", "saldrás", "saldrá", "saldremos", "saldréis", "saldrán"),
    ]
    être = [("être (être)", "Ser"), ("seré", "serás",
                                     "será", "seremos", "seréis", "serán")]

    avoir_posseder = [
        ("avoir_posseder", "Tener"),
        ("tendré", "tendrás", "tendrá", "tendremos", "tendréis", "tendrán"),
    ]
    apporter = [
        ("apporter", "traer"),
        ("traeré", "traerás", "traerá", "traeremos", "traeréis", "traerán"),
    ]
    venir = [
        ("venir", "venir"),
        ("vendré", "vendrás", "vendrá", "vendremos", "vendréis", "vendrán"),
    ]
    voir = [("voir", "ver"), ("veré", "verás",
                              "verá", "veremos", "veréis", "verán")]
    penser = [
        ("penser", "pensar"),
        ("pensaré", "pensarás", "pendará", "pensaremos", "pensaréis", "pensarán"),
    ]
    raconter = [
        ("raconter", "contar"),
        ("contaré", "contarás", "contará", "contaremos", "contaréis", "contarán"),
    ]

    demander = [
        ("demander", "pedir"),
        ("pediré", "pedirás", "pedirá", "pediremos", "pediréis", "pedirán"),
    ]
    sentir_ressentir = [
        ("sentir/ressentir", "Sentir"),
        ("sentiré", "sentirás", "sentirá", "sentiremos", "sentiréis", "sentirán"),
    ]
    dormir = [
        ("dormir", "dormir"),
        ("dormiré", "dormirás", "dormirá", "dormiremos", "dormiréis", "dormirán"),
    ]
    connaître = [
        ("connaître", "conocer"),
        ("conoceré", "conocerás", "conocerá",
         "conoceremos", "conoceréis", "conocerán"),
    ]
    déduire = [
        ("déduire", "deducir"),
        ("deduciré", "deducirás", "deducirá",
         "deduciremos", "deduciréis", "deducirán"),
    ]

    list_verbe = (
        marcher,
        dire,
        déduire,
        connaître,
        raconter,
        parler,
        demander,
        venir,
        donner,
        avoir_aux,
        tomber,
        dormir,
        faire,
        avoir_posseder,
        être_situation,
        être,
        manger,
        entendre,
        sentir_ressentir,
        mettre,
        vouloir_aimer,
        apporter,
        pouvoir,
        vivre,
        sortir,
        penser,
        aller,
        savoir,
        voir,
    )
    list_place = ("Yo", "tu", "el, ella", "nosotros",
                  "vosotros", "ellos, ellas")

elif temps == 7:
    parler = [
        ("parler", "hablar"),
        ("hablaría", "hablarías", "hablaría",
         "hablaríamos", "hablaríais", "hablarían"),
    ]
    marcher = [
        ("marcher", "andar"),
        ("andaría", "andarías", "andaría", "andaríamos", "andaríais", "andarían"),
    ]
    donner = [("donner", "dar"), ("daría", "darías",
                                  "daría", "daríamos", "daríais", "darían")]

    dire = [("dire", "decir"), ("diría", "dirías",
                                "diría", "diríamos", "diríais", "dirían")]
    être_situation = [
        ("être (se situer)", "Estar"),
        ("estaría", "estarías", "estaría", "estaríamos", "estaríais", "estarían"),
    ]
    faire = [("faire", "hacer"), ("haría", "harías",
                                  "haría", "haríamos", "haríais", "harían")]
    aller = [("aller", "ir"), ("iría", "irías",
                               "iría", "iríamos", "iríais", "irían")]
    manger = [
        ("manger", "Comer"),
        ("comería", "comerías", "comería", "comeríamos", "comeríais", "comerían"),
    ]
    vivre = [
        ("vivre", "vivir"),
        ("viviría", "vivirías", "viviría", "viviríamos", "viviríais", "vivirían"),
    ]
    tomber = [
        ("tomber", "caer"),
        ("caería", "caerías", "caería", "caeríamos", "caeríais", "caerían"),
    ]
    avoir_aux = [
        ("avoir (auxiliaire)", "haber"),
        ("habría", "habrías", "habría", "habríamos", "habríais", "habrían"),
    ]
    entendre = [("entendre", "oir"), ("oiría", "oirías",
                                      "oiría", "oiríamos", "oiríais", "oirían")]
    pouvoir = [
        ("pouvoir", "poder"),
        ("podría", "podrías", "podría", "podríamos", "podríais", "podrían"),
    ]
    mettre = [
        ("mettre", "poner"),
        ("pondría", "pondrías", "pondría", "pondríamos", "pondríais", "pondrían"),
    ]
    vouloir_aimer = [
        ("vouloir_aimer", "querer"),
        ("querría", "querrías", "querría", "querríamos", "querríais", "querrían"),
    ]
    savoir = [
        ("savoir", "saber"),
        ("sabría", "sabrías", "sabría", "sabríamos", "sabríais", "sabrían"),
    ]
    sortir = [
        ("sortir", "Salir"),
        ("saldría", "saldrías", "saldría", "saldríamos", "saldríais", "saldrían"),
    ]
    être = [("être (être)", "Ser"), ("sería", "serías",
                                     "sería", "seríamos", "seríais", "serían")]

    avoir_posseder = [
        ("avoir_posseder", "Tener"),
        ("tendría", "tendrías", "tendría", "tendríamos", "tendríais", "tendrían"),
    ]
    apporter = [
        ("apporter", "traer"),
        ("traería", "traerías", "traería", "traeríamos", "traeríais", "traerían"),
    ]
    venir = [
        ("venir", "venir"),
        ("vendría", "vendrías", "vendría", "vendríamos", "vendríais", "vendrían"),
    ]
    voir = [("voir", "ver"), ("vería", "verías",
                              "vería", "veríamos", "veríais", "verían")]
    penser = [
        ("penser", "pensar"),
        ("pensaría", "pensarías", "pendaría",
         "pensaríamos", "pensaríais", "pensarían"),
    ]
    raconter = [
        ("raconter", "contar"),
        ("contaría", "contarías", "contaría",
         "contaríamos", "contaríais", "contarían"),
    ]

    demander = [
        ("demander", "pedir"),
        ("pediría", "pedirías", "pediría", "pediríamos", "pediríais", "pedirían"),
    ]
    sentir_ressentir = [
        ("sentir/ressentir", "Sentir"),
        ("sentiría", "sentirías", "sentiría",
         "sentiríamos", "sentiríais", "sentirían"),
    ]
    dormir = [
        ("dormir", "dormir"),
        ("dormiría", "dormirías", "dormiría",
         "dormiríamos", "dormiríais", "dormirían"),
    ]
    connaître = [
        ("connaître", "conocer"),
        ("conocería", "conocerías", "conocería",
         "conoceríamos", "conoceríais", "conocerían"),
    ]
    déduire = [
        ("déduire", "deducir"),
        ("deduciría", "deducirías", "deduciría",
         "deduciríamos", "deduciríais", "deducirían"),
    ]

    list_verbe = (
        marcher,
        dire,
        déduire,
        connaître,
        raconter,
        parler,
        demander,
        venir,
        donner,
        avoir_aux,
        tomber,
        dormir,
        faire,
        avoir_posseder,
        être_situation,
        être,
        manger,
        entendre,
        sentir_ressentir,
        mettre,
        vouloir_aimer,
        apporter,
        pouvoir,
        vivre,
        sortir,
        penser,
        aller,
        savoir,
        voir,
    )
    list_place = ("Yo", "tu", "el, ella", "nosotros",
                  "vosotros", "ellos, ellas")

elif temps == 8:
    parler = [
        ("parler", "hablar"),
        ("hablando, hablado")
    ]
    marcher = [
        ("marcher", "andar"),
        ("andando, andado")
    ]
    donner = [("donner", "dar"), ("dando", "dado")]

    dire = [("dire", "decir"), ("diciendo", "dicho")]
    être_situation = [
        ("être (se situer)", "Estar"),
        ("estando", "estado")
    ]
    faire = [("faire", "hacer"), ("haciendo", "hecho")]
    aller = [("aller", "ir"), ("yendo", "ido")]
    manger = [
        ("manger", "Comer"),
        ("comiendo", "comido")
    ]
    vivre = [
        ("vivre", "vivir"),
        ("viviendo", "vivido"),
    ]
    tomber = [
        ("tomber", "caer"),
        ("cayendo", "caído"),
    ]
    avoir_aux = [
        ("avoir (auxiliaire)", "haber"),
        ("habiendo", "habido"),
    ]
    entendre = [("entendre", "oir"), ("oyendo", "oído")]
    pouvoir = [
        ("pouvoir", "poder"),
        ("pudiendo", "podido"),
    ]
    mettre = [
        ("mettre", "poner"),
        ("poniendo", "puesto"),
    ]
    vouloir_aimer = [
        ("vouloir_aimer", "querer"),
        ("queriendo", "querido"),
    ]
    savoir = [
        ("savoir", "saber"),
        ("sabiendo", "sabido"),
    ]
    sortir = [
        ("sortir", "Salir"),
        ("saliendo", "salido"),
    ]
    être = [("être (être)", "Ser"), ("siendo", "sido")]

    avoir_posseder = [
        ("avoir_posseder", "Tener"),
        ("teniendo", "tenido"),
    ]
    apporter = [
        ("apporter", "traer"),
        ("trayendo", "traído"),
    ]
    venir = [
        ("venir", "venir"),
        ("viniendo", "venido"),
    ]
    voir = [("voir", "ver"), ("viendo", "visto")]
    penser = [
        ("penser", "pensar"),
        ("pensando", "pensado"),
    ]
    raconter = [
        ("raconter", "contar"),
        ("contando", "contado"),
    ]

    demander = [
        ("demander", "pedir"),
        ("pidiendo", "pedido"),
    ]
    sentir_ressentir = [
        ("sentir/ressentir", "Sentir"),
        ("sintiendo", "sentido"),
    ]
    dormir = [
        ("dormir", "dormir"),
        ("durmiendo", "dormido"),
    ]
    connaître = [
        ("connaître", "conocer"),
        ("conociendo", "conocido"),
    ]
    déduire = [
        ("déduire", "deducir"),
        ("deduciendo", "deducido"),
    ]

    list_verbe = (marcher, dire, déduire, connaître, raconter, parler, demander, venir, donner, avoir_aux, tomber, dormir, faire, avoir_posseder,
                  être_situation, être, manger, entendre, sentir_ressentir, mettre, vouloir_aimer, apporter, pouvoir, vivre, sortir, penser, aller, savoir, voir,)
    list_place = ("g", "p.p.")

repeat = int(input("Combien de fois voulez-vous répéter la boucle ? "))
repeat_1 = repeat
points = 0

print(""), print("Si le verbe est au singulier, la couleur sera",
                 colored("bleue", "blue"))
print("Si le verbe est au pluriel, la couleur sera",
      colored("jaune", "yellow")), print("")

quit = False

while repeat_1 != 0:
    if len(list_place) > 2:
        print("")
        n_r_1 = random.randint(0, len(list_verbe) - 1)
        n_r_2 = random.randint(0, 1)
        list_place_random = random.randint(0, 5)
        verbe = list_verbe[n_r_1][0][n_r_2]

        n_r_person = random.randint(0, 5)
        person = str(list_place[n_r_person])

        response = str(list_verbe[n_r_1][1][n_r_person])
    else:
        print("")
        n_r_1 = random.randint(0, len(list_verbe) - 1)
        n_r_2 = random.randint(0, 1)
        list_place_random = random.randint(0, 5)
        verbe = list_verbe[n_r_1][0][n_r_2]

        n_r_person = random.randint(0, 1)
        person = str(list_place[n_r_person])

        response = str(list_verbe[n_r_1][1][n_r_person])

    if person[-1] == "Yo" or "tu" or "el, ella":
        phrase = (str(verbe), " à la ", color.BOLD,
                  str(colored(person, "blue")), color.END, " : ")
        result = input(phrase)
        result = str(result)
    elif person[-1] == "nosotros" or "vosotros" or "ellos, ellas":
        phrase = (str(verbe), " à la ", color.BOLD,
                  str(colored(person, "yellow")), color.END, " : ")
        result = str(input(phrase))

    if result == response:
        print(""), print(""), print(
            colored("**** Vous avez la bonne réponse ! ****", "green"))
        print("")
        print("")
        points += 1
        repeat_1 -= 1
        print(str(points), "/", str(repeat)
              ), print("Il reste", repeat_1, "questions")

    elif result == "quit":
        repeat_1 = 0
        quit = True
        print(""), print(
            "Oh... vous partez déjà ? Et bien à une prochaine fois alors !")
        print("")

    else:
        print("")
        print(str(colored("Vous avez la mauvaise réponse", "red")),
              ". La bonne réponse était:", response)
        print("")
        print("")
        repeat_1 -= 1
        print(str(points), "/", str(repeat))
        print("Il reste", repeat_1, "questions")

if points >= 1 and quit != True:
    if repeat == 10:
        print("Vous avez eu ", str(points), "/", str(repeat)), print("")
    elif repeat < 10 and repeat != 0:
        ten = points * 10 / repeat
        print(
            "Vous avez eu ", str(
                points), "/", str(repeat), ". Ce qui est l'équivalent de: ", str(ten), "/10"
        ), print("")
    elif repeat > 10:
        twenty = points * 20 / repeat
        print(
            "Vous avez eu ", str(
                points), "/", str(repeat), ". Ce qui est l'équivalent de: ", str(twenty), "/20"
        ), print("")

# ó
# í
# á
