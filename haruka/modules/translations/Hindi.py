
RUN_STRINGS = (

    "Where do you think you're going?",

    "Huh? what? did they get away?",

    "ZZzzZZzz... Huh? what? oh, just them again, nevermind.",

    "Get back here!",

    "Not so fast...",

    "Look out for the wall!",

    "Don't leave me alone with them!!",

    "You run, you die.",

    "Jokes on you, I'm everywhere",

    "You're gonna regret that...",

    "You could also try /kickme, I hear that's fun.",

    "Go bother someone else, no-one here cares.",

    "You can run, but you can't hide.",

    "Is that all you've got?",

    "I'm behind you...",

    "You've got company!",

    "We can do this the easy way, or the hard way.",

    "You just don't get it, do you?",

    "Yeah, you better run!",

    "Please, remind me how much I care?",

    "I'd run faster if I were you.",

    "That's definitely the droid we're looking for.",

    "May the odds be ever in your favour.",

    "Famous last words.",

    "And they disappeared forever, never to be seen again.",

    "\"Oh, look at me! I'm so cool, I can run from a bot!\" - this person",

    "Yeah yeah, just tap /kickme already.",

    "Here, take this ring and head to Mordor while you're at it.",

    "Legend has it, they're still running...",

    "Unlike Harry Potter, your parents can't protect you from me.",

    "Fear leads to anger. Anger leads to hate. Hate leads to suffering. If you keep running in fear, you might "

    "be the next Vader.",

    "Multiple calculations later, I have decided my interest in your shenanigans is exactly 0.",

    "Legend has it, they're still running.",

    "Keep it up, not sure we want you here anyway.",

    "You're a wiza- Oh. Wait. You're not Harry, keep moving.",

    "NO RUNNING IN THE HALLWAYS!",

    "Hasta la vista, baby.",

    "Who let the dogs out?",

    "It's funny, because no one cares.",

    "Ah, what a waste. I liked that one.",

    "Frankly, my dear, I don't give a damn.",

    "My milkshake brings all the boys to yard... So run faster!",

    "You can't HANDLE the truth!",

    "A long time ago, in a galaxy far far away... Someone would've cared about that. Not anymore though.",

    "Hey, look at them! They're running from the inevitable banhammer... Cute.",

    "Han shot first. So will I.",

    "What are you running after, a white rabbit?",

    "As The Doctor would say... RUN!",

)
MARKDOWN_HELP = """

मार्कडाउन टेलीग्राम द्वारा समर्थित एक बहुत शक्तिशाली स्वरूपण उपकरण है।  {}कुछ सुधार हैं, यह सुनिश्चित करने के लिए कि सहेजे गए नोटों को सही ढंग से पार्स किया गया है और आपको बटन बनाने की अनुमति है।

- <code> _cursiva_ </ code>: यदि पाठ '_' के बीच दर्ज किया गया है, तो यह इटैलिक में पाठ उत्पन्न करेगा- 
<Code> * बोल्ड * </ कोड>: यदि पाठ '*' के बीच दर्ज किया गया है, तो यह बोल्ड में पाठ उत्पन्न करेगा- < code> `कोड` </ code>:` `'के बीच पाठ में प्रवेश करने से एक अखंड पाठ उत्पन्न होगा, जिसे' कोड'- <कोड> [कुछ पाठ] (someURL) </ कोड> के रूप में भी जाना जाता है: यह एक लिंक बनाएगा -  संदेश <code> someext </ code>, में प्रदर्शित किया जाएगा और उस पर क्लिक करने से आप उस पृष्ठ पर पहुंच जाएंगे, जिसे आपने <code> someurL </ code>। EX: <कोड> [test] (example.com) <पर क्लिक किया है।  / कोड>

- <कोड> [बटन ] (buttonurl: someURL) </ code>: यह एक विशेष वृद्धि है जो उपयोगकर्ताओं को टेलीग्राम बटन की अनुमति देता है।  <code> bottontext </ code> वह नाम होगा जो बटन पर दिखाई देता है, और <code> someURL </ code> \ वेब पेज या URL होगा जो ईजी दबाने पर खोला जाएगा: <कोड> [यह एक बटन है  (buttonurl: example.com)
 </code> यदि आप एक ही पंक्ति में कई बटन लगाना चाहते हैं, तो उपयोग करें: एक जैसे, यहाँ: <code> [one] (buttonurl://example.com) [two] (buttonurl: //google.com:same) </ code> यह प्रत्येक लाइन पर एक के बजाय एक ही लाइन पर दो बटन बनाएगा। 
"""
HindiStrings{
#Connections
    "Disabled connections to this chat for users": "Conexiones deshabilitadas en este chat para los usuarios",
    "Enabled connections to this chat for users": "Conexiones habilitadas en este chat para los usuarios",
    "Please enter on/yes/off/no in group!": "Por favor escribe on/yes/off/no en el grupo!",
    "Successfully connected to *{}*": "Conectado correctamente a *{}*",
    "Connection failed!": "Conexión fallida!",
    "Connections to this chat not allowed!": "Conexiones no permitidas en este chat!",
    "Write chat ID to connect!": "Escribe el ID del chat para conectar!",
    "Usage limited to PMs only!": "Uso restringido solo a mensajes privados",

#Misc
    "RUNS-K": RUN_STRINGS,
    "SLAP_TEMPLATES-K": SLAP_TEMPLATES,
    "ITEMS-K": ITEMS,
    "HIT-K": HIT,
    "THROW-K": THROW,
    "ITEMP-K": ITEMS,
    "ITEMR-K": ITEMS,
    "MARKDOWN_HELP-K": MARKDOWN_HELP,

    "The original sender, {}, has an ID of `{}`.\nThe forwarder, {}, has an ID of `{}`.":
        "El remitente, {}, tiene el ID `{}`.\nEl receptor, {}, tiene el ID `{}`.",
    "{}'s id is `{}`.": "ID {} - `{}`.",
    "Your id is `{}`.": "Tu ID - `{}`.",
    "This group's id is `{}`.": "ID de este grupo - `{}`.",

    "I can't extract a user from this.": "No puedo recuperar el ID de este usuario",
    "<b>User info</b>:": "<b>Información del usuario</b>:",
    "\nFirst Name: {}": "\nNombre: {}",
    "\nLast Name: {}": "\nApellido: {}",
    "\nUsername: @{}": "\nNombre de usuario: @{}",
    "\nPermanent user link: {}": "\nLink permanente del usuario: {}",
    "\n\nThis person is my owner - I would never do anything against them!":
        "\n\nEsta persona es mi dueñ@, nunca haría nada contra él/ella!",
    "\nThis person is one of my sudo users! Nearly as powerful as my owner - so watch it.":
        "\nEsta persona es un@ de mis usuari@s sudo! Casi con tanto poder como mi dueñ@, así que ten cuidado",
    "\nThis person is one of my support users! Not quite a sudo user, but can still gban you off the map.":
        "\nEsta persona es uno de mis usuarios con derechos. No es como un usuario sudo, pero te puede dar global ban, ten cuidado!",
    "\nThis person has been whitelisted! That means I'm not allowed to ban/kick them.":
        "\nEsta persona está en la lista blanca. Esto signidica que no puedo banearla ni echarla.",

    "Its always banhammer time for me!": "Siempre es la hora banhammer para mi!",

    "It's {} in {}": "Está {} en {}",

    "Please reply to a sticker to get its ID.": "Por favor responde a un stciker para obtener su ID.",
    "Please reply to a sticker for me to upload its PNG.": "Por favor, responde a un sticker para que pueda subir su PNG .",

    "Write a location to check the weather.": "Escribe una ubicación para ver que tiempo hace.",
    "I will keep an eye on both happy and sad times!": "Estaré aquí en las buenas y en las malas!",
    "Today in {} is being {}, around {}°C.\n": "Hoy en {} hace {}, alrededor de {}°C.\n",
    "Sorry, location not found.": "Lo siento, ubicación no encontrada.",

    "Deleting identifiable data...": "Borrando datos de usuario...",

    "Try forwarding the following message to me, and you'll see!":
        "Prueba a enviarme el siguiente mensaje y lo verás!",
    "/save test This is a markdown test. _italics_, *bold*, `code`, [URL](example.com) [button](buttonurl:github.com) [button2](buttonurl://google.com:same)":
    """/save test Esto es un test de markdown. _cursiva_, *negrita*, `codigo`, \
[URL](example.com) 
[Botón](buttonurl:github.com)
[Botón2](buttonurl://google.com:same)""",

#Misc GDPR
"send-gdpr": """Tu información personal ha sido borrada.\n\nTen en cuento que esto no te va a desbanear \
de ningún chat, ya que eso son datos de Telegram, NO datos de YanaBot.
Flooding, advertencias, y bans globales también se conservan, a partir de \
[esto](https://ico.org.uk/for-organisations/guide-to-the-general-data-protection-regulation-gdpr/individual-rights/right-to-erasure/), "
que establece claramente que el derecho de cancelación no se aplica \
\"para la realización de una tarea realizada en interés público.\", así como \
el caso de los datos mencionados anteriormente.""",

#Admin
"How am I meant to promote someone that's already an admin?": "¿Como voy a ascender a administrador a alguien que ya lo es?",
"I can't promote myself! Get an admin to do it for me.": "¡No puedo hacerme administradora a mi misma! ¡Avisa a algún administrador para que lo haga!",
"Successfully promoted in *{}*!": " Ascendido a administrador en *{}*!",

"This person CREATED the chat, how would I demote them?": "Esta persona ha creado el chat. ¿Cómo quieres que le quite el admin?",
"Can't demote what wasn't promoted!": "No puedo quitarle el admin si no lo tiene!",
"I can't demote myself!": "No puedo quitarme de ser administradora yo misma!",
"Successfully demoted in *{}*!": "Ya no es administrador en *{}*!",
"Could not demote. I might not be admin, or the admin status was appointed by another user, so I can't act upon them!": 
"No puedo quitarle el admin. Puede que no sea administrador o que el estado de administrador fuese dado por otro usuario, asi que no puedo actuar sobre él!",

"I don't have access to the invite link, try changing my permissions!": "No tengo acceso al link de invitación, prueba cambiando mis permisos!",
"I can only give you invite links for supergroups and channels, sorry!": "Lo siento, solo puedo dar links de invitación para supergrupos y canales.",

"Admins in": "Administradores en",
"this chat": "este chat",
" (Creator)": " (Creador)",

#AFK
"{} is now AFK!": "Ahora {} está ausente!",
"{} is no longer AFK!": "{} ya no está ausente!",
"{} is AFK!": "{} está ausente!",
"{} is AFK! says its because of: \n{}": "{} está ausente! Dice que es porque: \n{}",

#Antiflood
"I like to leave the flooding to natural disasters. But you, you were just a disappointment. Get out.":
     "Suelo tener bastante paciencia con la gente pesada, pero te has pasado. ¡Largo de aquí!",
"I can't kick people here, give me permissions first! Until then, I'll disable antiflood.":
    "No puedo expulsar a la gente aquí, dame permisos primero! Hasta que eso ocurra deshabilitaré el antiflood.",
"Antiflood has been disabled.": "Antiflood ha sido deshabilitado.",
"Antiflood has to be either 0 (disabled), or a number bigger than 3 (enabled)!":
    "Antiflood tiene que ser 0 (deshabilitado), o un número superior a 3 (habilitado)!",
"Antiflood has been updated and set to {}": "Antiflood se ha actualizado y ha sido establecido a {}",
"Unrecognised argument - please use a number, 'off', or 'no'.":
    "Comando desconocido- por favor usa un número, 'off', o 'no'.",
"I'm not currently enforcing flood control!": "Ahora mismo no estoy no controlando el flood!",
"I'm currently banning users if they send more than {} consecutive messages.":
     "Estoy baneando a todos los usuarios que envíen más de {} mensajes consecutivos.",

#Antispam
"I've enabled antispam security in this group. This will help protect you from spammers, unsavoury characters, and the biggest trolls.":
 "He activado la seguridad antispam en este grupo. Esto te ayudará a protegerte contra spammers, personas desagradables y trolls.",

"I've disabled antispam security in this group. GBans wont affect your users anymore. You'll be less protected from any trolls and spammers though!":
    "He desactivado la seguridad antispam en este grupo. Los Bans Globales no afectarán a los usuarios. Estarás menos protegido de trolls y spammers!",

"Give me some arguments to choose a setting! on/off, yes/no!\n\nYour current setting is: {}\nWhen True, any gbans that happen will also happen in your group. When False, they won't, leaving you at the possible mercy of spammers.":
    "Dame algún comando para establecer la configuración! on/off, yes/no!\n\nTu configuración actual es: {}\nCuando sea True, cualquier Ban Global que ocurra tambien ocurrirá en tu grupo. Cuando sea False, los Ban Globales no afectarán en tu grupo, dejandolo a merced de posibles spammers.",

"Globally banned: <b>{}</b>": "Baneado globalmente: <b>{}</b>",
"\nGlobally muted: <b>{}</b>": "\nSilenciado globalmente: <b>{}</b>",
"\nReason: {}": "\nRazón: {}",

}

