print("Enter Nerd")
verb_input = input()
#print("AR, ER, or IR")
#r_input = input()
print("Enter Tense")
tense_input = input()
print("Enter Conjugation")
conjugation_input = input()
#def process_ra(ra):
# if ra == "ar" or ra == "Ar" or ra == "AR":
#   ar_form = True
#  print("ar")
#  elif ra == "er" or ra == "Er" or ra == "ER":
#   er_form = True
#  print("er")
#elif ra == "ir" or ra == "Ir" or ra == "IR":
# ir_form = True
#print("ir")
# else:
#print("invalid")
# bruh = ("terminated")
#return
def process_esnet(esnet):
    global imp_form
    global pret_form
    global pres_form
    global fut_form
    global con_form
    if esnet == "imperfect" or esnet == "imp" or esnet == "Imperfect":
        imp_form = True
        pret_form = False
        pres_form = False
        fut_form = False
        con_form = False
    elif esnet == "preterite" or esnet == "pret" or esnet == "Preterite":
        pret_form = True
        pres_form = False
        fut_form = False
        con_form = False
        imp_form = False
    elif esnet == "present" or esnet == "pres" or esnet == "Present":
        pres_form = True
        fut_form = False
        con_form = False
        imp_form = False
        pret_form = False
    elif esnet == "future" or esnet == "fut" or esnet == "Future":
        fut_form = True
        con_form = False
        imp_form = False
        pret_form = False
        pres_form = False
    elif esnet == "conditional" or esnet == "cond" or esnet == "Conditional":
        con_form = True
        imp_form = False
        pret_form = False
        pres_form = False
        fut_form = False
    else:
        print("invalid")
        bruh = ("terminated")
    return


def process_conj(conj):
    global yo_form
    global tu_form
    global el_form
    global nos_form
    global vos_form
    global ellos_form
    if conj == "yo" or conj == "Yo":
        yo_form = True
        tu_form = False
        el_form = False
        nos_form = False
        vos_form = False
        ellos_form = False
    elif conj == "tu" or conj == "Tu":
        tu_form = True
        yo_form = False
        el_form = False
        nos_form = False
        vos_form = False
        ellos_form = False
    elif conj == "el" or conj == "El" or conj == "ella" or conj == "Ella" or conj == "usted" or conj == "Usted":
        el_form = True
        yo_form = False
        tu_form = False
        nos_form = False
        vos_form = False
        ellos_form = False
    elif conj == "nosotros" or conj == "Nosotros":
        nos_form = True
        yo_form = False
        tu_form = False
        el_form = False
        vos_form = False
        ellos_form = False
    elif conj == "vosotros" or conj == "Vosotros":
        vos_form = True
        yo_form = False
        tu_form = False
        el_form = False
        nos_form = False
        ellos_form = False
    elif conj == "ellos" or conj == "Ellos" or conj == "ellas" or conj == "Ellas" or conj == "ustedes" or conj == "Ustedes":
        ellos_form = True
        yo_form = False
        tu_form = False
        el_form = False
        nos_form = False
        vos_form = False
    else:
        print("invalid tense")
        global bruh
        bruh = ("terminated")
    return


def arerir(r):
    global arform
    global erform
    global irform
    if r != "sdfjkldfdisfhdfhasfdhl":
        vi = verb_input
        area = "ar"
        erea = "er"
        irea = "ir"
        if area in vi:
            arform = True
            erform = False
            irform = False
        elif erea in vi:
            erform = True
            arform = False
            irform = False
        elif irea in vi:
            irform = True
            arform = False
            erform = False
        else:
            print("invalid")
        return


arerir(verb_input)
process_esnet(tense_input)
process_conj(conjugation_input)
present_ar_yo = "o"
present_ar_tu = "as"
present_ar_el = "a"
present_ar_nos = "amos"
present_ar_vos = "áis"
present_ar_ellos = "an"
present_er_yo = "o"
present_er_tu = "es"
present_er_el = "e"
present_er_nos = "emos"
present_er_vos = "éis"
present_er_ellos = "en"
present_ir_yo = "o"
present_ir_tu = "es"
present_ir_el = "e"
present_ir_nos = "imos"
present_ir_vos = "ís"
present_ir_ellos = "en"

preterite_ar_yo = "é"
preterite_ar_tu = "aste"
preterite_ar_el = "ó"
preterite_ar_nos = "amos"
preterite_ar_vos = "asteis"
preterite_ar_ellos = "aron"
preterite_eir_yo = "í"
preterite_eir_tu = "iste"
preterite_eir_el = "ió"
preterite_eir_nos = "imos"
preterite_eir_vos = "isteis"
preterite_eir_ellos = "ieron"

imperfect_ar_yo = "aba"
imperfect_ar_tu = "abas"
imperfect_ar_el = "aba"
imperfect_ar_nos = "ábamos"
imperfect_ar_vos = "abais"
imperfect_ar_ellos = "aban"
imperfect_eir_yo = "ía"
imperfect_eir_tu = "ías"
imperfect_eir_el = "ía"
imperfect_eir_nos = "íamos"
imperfect_eir_vos = "íais"
imperfect_eir_ellos = "ían"

future_aeir_yo = "é"
future_aeir_tu = "ás"
future_aeir_el = "á"
future_aeir_nos = "emos"
future_aeir_vos = "éis"
future_aeir_ellos = "án"

conditional_aeir_yo = "ía"
conditional_aeir_tu = "ías"
conditional_aeir_el = "ía"
conditional_aeir_nos = "íamos"
conditional_aeir_vos = "íais"
conditional_aeir_ellos = "ían"

if arform is True and pres_form is True and yo_form is True:
    final = verb_input.replace("ar", "")
    print(final + present_ar_yo)
elif arform is True and pres_form is True and tu_form is True:
    final = verb_input.replace("ar", "")
    print(final + present_ar_tu)
elif arform is True and pres_form is True and el_form is True:
    final = verb_input.replace("ar", "")
    print(final + present_ar_el)
elif arform is True and pres_form is True and nos_form is True:
    final = verb_input.replace("ar", "")
    print(final + present_ar_nos)
elif arform is True and pres_form is True and vos_form is True:
    final = verb_input.replace("ar", "")
    print(final + present_ar_vos)
elif arform is True and pres_form is True and ellos_form is True:
    final = verb_input.replace("ar", "")
    print(final + present_ar_ellos)

elif erform is True and pres_form is True and yo_form is True:
    final = verb_input.replace("er", "")
    print(final + present_er_yo)
elif erform is True and pres_form is True and tu_form is True:
    final = verb_input.replace("er", "")
    print(final + present_er_tu)
elif erform is True and pres_form is True and el_form is True:
    final = verb_input.replace("er", "")
    print(final + present_er_el)
elif erform is True and pres_form is True and nos_form is True:
    final = verb_input.replace("er", "")
    print(final + present_er_nos)
elif erform is True and pres_form is True and vos_form is True:
    final = verb_input.replace("er", "")
    print(final + present_er_vos)
elif erform is True and pres_form is True and ellos_form is True:
    final = verb_input.replace("er", "")
    print(final + present_er_ellos)

elif irform is True and pres_form is True and yo_form is True:
    final = verb_input.replace("ir", "")
    print(final + present_ir_yo)
elif irform is True and pres_form is True and tu_form is True:
    final = verb_input.replace("ir", "")
    print(final + present_ir_tu)
elif irform is True and pres_form is True and el_form is True:
    final = verb_input.replace("ir", "")
    print(final + present_ir_el)
elif irform is True and pres_form is True and nos_form is True:
    final = verb_input.replace("ir", "")
    print(final + present_ir_nos)
elif irform is True and pres_form is True and vos_form is True:
    final = verb_input.replace("ir", "")
    print(final + present_ir_vos)
elif irform is True and pres_form is True and ellos_form is True:
    final = verb_input.replace("ir", "")
    print(final + present_ir_ellos)

elif arform is True and pret_form is True and yo_form is True:
    final = verb_input.replace("ar", "")
    print(final + preterite_ar_yo)
elif arform is True and pret_form is True and tu_form is True:
    final = verb_input.replace("ar", "")
    print(final + preterite_ar_tu)
elif arform is True and pret_form is True and el_form is True:
    final = verb_input.replace("ar", "")
    print(final + preterite_ar_el)
elif arform is True and pret_form is True and nos_form is True:
    final = verb_input.replace("ar", "")
    print(final + preterite_ar_nos)
elif arform is True and pret_form is True and vos_form is True:
    final = verb_input.replace("ar", "")
    print(final + preterite_ar_vos)
elif arform is True and pret_form is True and ellos_form is True:
    final = verb_input.replace("ar", "")
    print(final + preterite_ar_ellos)

elif erform is True and pret_form is True and yo_form is True:
    final = verb_input.replace("er", "")
    print(final + preterite_eir_yo)
elif erform is True and pret_form is True and tu_form is True:
    final = verb_input.replace("er", "")
    print(final + preterite_eir_tu)
elif erform is True and pret_form is True and el_form is True:
    final = verb_input.replace("er", "")
    print(final + preterite_eir_el)
elif erform is True and pret_form is True and nos_form is True:
    final = verb_input.replace("er", "")
    print(final + preterite_eir_nos)
elif erform is True and pret_form is True and vos_form is True:
    final = verb_input.replace("er", "")
    print(final + preterite_eir_vos)
elif erform is True and pret_form is True and ellos_form is True:
    final = verb_input.replace("er", "")
    print(final + preterite_eir_ellos)

elif irform is True and pret_form is True and yo_form is True:
    final = verb_input.replace("ir", "")
    print(final + preterite_eir_yo)
elif irform is True and pret_form is True and tu_form is True:
    final = verb_input.replace("ir", "")
    print(final + preterite_eir_tu)
elif irform is True and pret_form is True and el_form is True:
    final = verb_input.replace("ir", "")
    print(final + preterite_eir_el)
elif irform is True and pret_form is True and nos_form is True:
    final = verb_input.replace("ir", "")
    print(final + preterite_eir_nos)
elif irform is True and pret_form is True and vos_form is True:
    final = verb_input.replace("ir", "")
    print(final + preterite_eir_vos)
elif irform is True and pret_form is True and ellos_form is True:
    final = verb_input.replace("ir", "")
    print(final + preterite_eir_ellos)

elif arform is True and imp_form is True and yo_form is True:
    final = verb_input.replace("ar", "")
    print(final + imperfect_ar_yo)
elif arform is True and imp_form is True and tu_form is True:
    final = verb_input.replace("ar", "")
    print(final + imperfect_ar_tu)
elif arform is True and imp_form is True and el_form is True:
    final = verb_input.replace("ar", "")
    print(final + imperfect_ar_el)
elif arform is True and imp_form is True and nos_form is True:
    final = verb_input.replace("ar", "")
    print(final + imperfect_ar_nos)
elif arform is True and imp_form is True and vos_form is True:
    final = verb_input.replace("ar", "")
    print(final + imperfect_ar_vos)
elif arform is True and imp_form is True and ellos_form is True:
    final = verb_input.replace("ar", "")
    print(final + imperfect_ar_ellos)

elif erform is True and imp_form is True and yo_form is True:
    final = verb_input.replace("er", "")
    print(final + imperfect_eir_yo)
elif erform is True and imp_form is True and tu_form is True:
    final = verb_input.replace("er", "")
    print(final + imperfect_eir_tu)
elif erform is True and imp_form is True and el_form is True:
    final = verb_input.replace("er", "")
    print(final + imperfect_eir_el)
elif erform is True and imp_form is True and nos_form is True:
    final = verb_input.replace("er", "")
    print(final + imperfect_eir_nos)
elif erform is True and imp_form is True and vos_form is True:
    final = verb_input.replace("er", "")
    print(final + imperfect_eir_vos)
elif erform is True and imp_form is True and ellos_form is True:
    final = verb_input.replace("er", "")
    print(final + imperfect_eir_ellos)

elif irform is True and imp_form is True and yo_form is True:
    final = verb_input.replace("ir", "")
    print(final + imperfect_eir_yo)
elif irform is True and imp_form is True and tu_form is True:
    final = verb_input.replace("ir", "")
    print(final + imperfect_eir_tu)
elif irform is True and imp_form is True and el_form is True:
    final = verb_input.replace("ir", "")
    print(final + imperfect_eir_el)
elif irform is True and imp_form is True and nos_form is True:
    final = verb_input.replace("ir", "")
    print(final + imperfect_eir_nos)
elif irform is True and imp_form is True and vos_form is True:
    final = verb_input.replace("ir", "")
    print(final + imperfect_eir_vos)
elif irform is True and imp_form is True and ellos_form is True:
    final = verb_input.replace("ir", "")
    print(final + imperfect_eir_ellos)

elif arform is True and fut_form is True and yo_form is True:
    final = verb_input
    print(final + future_aeir_yo)
elif arform is True and fut_form is True and tu_form is True:
    final = verb_input
    print(final + future_aeir_tu)
elif arform is True and fut_form is True and el_form is True:
    final = verb_input
    print(final + future_aeir_el)
elif arform is True and fut_form is True and nos_form is True:
    final = verb_input
    print(final + future_aeir_nos)
elif arform is True and fut_form is True and vos_form is True:
    final = verb_input
    print(final + future_aeir_vos)
elif arform is True and fut_form is True and ellos_form is True:
    final = verb_input
    print(final + future_aeir_ellos)

elif erform is True and fut_form is True and yo_form is True:
    final = verb_input
    print(final + future_aeir_yo)
elif erform is True and fut_form is True and tu_form is True:
    final = verb_input
    print(final + future_aeir_tu)
elif erform is True and fut_form is True and el_form is True:
    final = verb_input
    print(final + future_aeir_el)
elif erform is True and fut_form is True and nos_form is True:
    final = verb_input
    print(final + future_aeir_nos)
elif erform is True and fut_form is True and vos_form is True:
    final = verb_input
    print(final + future_aeir_vos)
elif erform is True and fut_form is True and ellos_form is True:
    final = verb_input
    print(final + future_aeir_ellos)

elif irform is True and fut_form is True and yo_form is True:
    final = verb_input
    print(final + future_aeir_yo)
elif irform is True and fut_form is True and tu_form is True:
    final = verb_input
    print(final + future_aeir_tu)
elif irform is True and fut_form is True and el_form is True:
    final = verb_input
    print(final + future_aeir_el)
elif irform is True and fut_form is True and nos_form is True:
    final = verb_input
    print(final + future_aeir_nos)
elif irform is True and fut_form is True and vos_form is True:
    final = verb_input
    print(final + future_aeir_vos)
elif irform is True and fut_form is True and ellos_form is True:
    final = verb_input
    print(final + future_aeir_ellos)

elif arform is True and con_form is True and yo_form is True:
    final = verb_input
    print(final + conditional_aeir_yo)
elif arform is True and con_form is True and tu_form is True:
    final = verb_input
    print(final + conditional_aeir_tu)
elif arform is True and con_form is True and el_form is True:
    final = verb_input
    print(final + conditional_aeir_el)
elif arform is True and con_form is True and nos_form is True:
    final = verb_input
    print(final + conditional_aeir_nos)
elif arform is True and con_form is True and vos_form is True:
    final = verb_input
    print(final + conditional_aeir_vos)
elif arform is True and con_form is True and ellos_form is True:
    final = verb_input
    print(final + conditional_aeir_ellos)

elif erform is True and con_form is True and yo_form is True:
    final = verb_input
    print(final + conditional_aeir_yo)
elif erform is True and con_form is True and tu_form is True:
    final = verb_input
    print(final + conditional_aeir_tu)
elif erform is True and con_form is True and el_form is True:
    final = verb_input
    print(final + conditional_aeir_el)
elif erform is True and con_form is True and nos_form is True:
    final = verb_input
    print(final + conditional_aeir_nos)
elif erform is True and con_form is True and vos_form is True:
    final = verb_input
    print(final + conditional_aeir_vos)
elif erform is True and con_form is True and ellos_form is True:
    final = verb_input
    print(final + conditional_aeir_ellos)

elif irform is True and con_form is True and yo_form is True:
    final = verb_input
    print(final + conditional_aeir_yo)
elif irform is True and con_form is True and tu_form is True:
    final = verb_input
    print(final + conditional_aeir_tu)
elif irform is True and con_form is True and el_form is True:
    final = verb_input
    print(final + conditional_aeir_el)
elif irform is True and con_form is True and nos_form is True:
    final = verb_input
    print(final + conditional_aeir_nos)
elif irform is True and con_form is True and vos_form is True:
    final = verb_input
    print(final + conditional_aeir_vos)
elif irform is True and con_form is True and ellos_form is True:
    final = verb_input
    print(final + conditional_aeir_ellos)