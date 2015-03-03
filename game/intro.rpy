
# The game starts here.
label start:
    scene bg castle_exterior with fade
    show princess at midleft with moveinleft
    p "Finally. You’d think that if they were going to hold some dragons captive, they would hold them in a place more accessible to princesses who want to harness their power for more important things!"
    p "But first... I’ll have to deal with the mage in charge."
    show cyril at midright with moveinright
    p "... what. They put a kid in charge?! This is exactly the kind of inefficiency I intend to remedy when I am queen!"
    p "Still… I’ll have to deal with him somehow."
    c "Biggeldy, boggaldy, wap!"
    c "I knew I didn't get that spell right!  If only I could remember how that went.  Biggeldy, boggaldy, wu?  Boggaldy, biggaldy... hmmm... I'm not even sure that I'm using the proper words."
    c "Oh!  Hello!"
    menu:
        "Play it sweet":
            jump sweet
        "Tell him the truth":
            jump truth
        "Ignore him.":
            jump ignore
        
            
label sweet:
    p "Oh hello! You must be in charge here. How lovely to make your acquaintance, Mr...?"
    c "Merlonious.  Cyril Merlonious.  At least, the last time somebody called me it.  Which has been a while come to think of it.  "
    c "Erm, wait a moment... it's you.  Princess!  I almost didn't recognize you!  Your majesty!  Did you find someone to relieve me?  Is that why you're here?"
    c "I did so know this day would come."
    p "Yes, Moronious. Yes, I am here to relieve you. It’s quite a demotion for me, but well, one must perform one’s royal duties. So if you’ll just show me around, then you can be on your way and leave these… dragons in my care."
    c "I can't tell you how happy I am to hear that!  I didn't think this day will come.  I must send word- oh!  I just need the royal seal from you.  Have you spoken with the council of mages?  Is everything in order?"
    p "Oh, how dreadful! They didn’t send me with it! They must have assumed that any person of intelligence would immediately see my royal person and know to do whatever I say."
    c "Of course.  But it is the custom, and you know what they say about rules being meant to be followed and all that gobbledy-spook that I think I remembered once.  Ah, well."
    p "Perhaps I could come in out of the rain, and stay until we can get everything sorted out?"
    c "Well, I guess I haven't had company in quite some time.  And it does get rather dreary with those dragons questioning me.  Come in, yes.  Come in."
    p "The dragons? What can you tell me about them?"
    c "Well, many of them have left actually.  Love can do wonders to reform a rogue dragon.  One got placed in the castle due to his insatiable lust for destruction.  I think.  He has been here a long time and my master told me a little of him before he passed.  My master was really wonderful.  He took good care of these dragons. Cared about their heart.  There's another as well, more recent an addition.  He was kidnapping ladies in the marketplace just for fun apparently.  Causing all sorts of trouble until he had to be locked away."
    p "Oh my, that sounds dreadful! And yet also intriguing. Would you introduce me?"

label truth:
    p "I’m here to retake my rightful throne. Assist me, and be rewarded. Hinder me, and feel my wrath."
    c "Oh, it's you.  Princess!  I almost didn't recognize you!  Your majesty!  I ummm... I most certainly don't want to hinder you.  But I am awfully confused to how I, a humble servant of Dyconis could help you." #TODO: Is Dyconis the name we want to use here? Make sure this is consistent.
    p "I’m wet, cold, and tired. I need the warmest room in this dreadful castle and a hot bath. If you can’t arrange that, then you are useless to me and had best begone."
    c "Ah, erm, yes of course your majesty!  A bath is coming right up!  And a room.  Well, my room is the warmest room, but if you give me some time to relocate I'm sure I could find somewhere else to settle for the moment."
    p "That is acceptable. You may lead me there now."
    c "So, this is the castle of the banished.  It hasn't been visited in quite some time.  Or cleaned actually.  Hehehe.  I didn't expect company so I hadn't thought about cleaning.  I suppose I had better get to that.  I do not have any bath salts either, but we have no shortage of warm water here.  That's for certain."
    p "Yes, yes. Now, what can you tell me about the other… residents of this place?"
    c "It is just me.  Well, and the dragons.  But they are here from their punishment.  Kidnapping ladies is not a very delightful business I do say.  "
    c "Usually I find I must ignore them or they will try to plead their case.  Well, they don't really do that.  They more mock- anyway.  What brings you here again?"
    menu:
        "Make up something flattering.":
            jump flattering
        "Tell the truth.":
            jump truth2 
            
label truth2:
    p "Unfortunately, I find myself in the unenviable position of needing assistance from others to claim the crown that has been wrenched from my rightful hands."
    c "Oh, that is rather disappointing.  But as I believe, you were never in line for the throne?  Is that right?  It was that other girl?  That sister of yours?  "
    c "I do hope I got my facts right.  I'm incredibly mixed up these days.  Don't know my right from my left and my left from my right."
    p "Clearly. You’d best leave the facts to me and concentrate on doing my bidding."
    c "I am sorry to have offended you Princess, I must leave it to you.  Is this to your liking?"
    p "Is this really the best room here?"
    jump room_intro

label flattering:
    p "Believe it or not, I was thinking about... you."
    p "Doesn’t it get terribly lonely out here? Don’t you often find yourself wishing for companionship? I try to meet the needs of all the citizens of our realm, as part of my royal duties. Surely there’s something I could help you with..."
    c "Oh erm... you don't say..."
    c "I guess I... I mean as much as anyone... I mean... Oh.  It's a very thoughtful offer from you, surely."
    p "I’m certain we could help each other. But for now...is this really the best room you have?"
    jump room_intro
    
label room_intro:
    c "It is.  Well, I’ve tried to make it as comfortable as possible.  I have a few keepsakes from home in it and my frilly rug which does keep it warm in the middle of the cold snap.  "
    c "And it is close to the dragons so I can regularly keep watch over them, as I am supposed to.  Would you like to be somewhere further away?  This is a large castle."
    p "No, no, this will do. You may leave me for now, but I may need your assistance later."
    c "Yes, yes.  I will get right to running that bath for you my majesty. I mean your majesty!  Your majesty.  Because you are most certainly not mine... errr... I will see to that bath."
    "..."
    #SHOWER
    
    "(That’s better! One of these days I will need to look into learning more weather magic...awful that I should be drenched at the whim of the mere skies)."
    "(But now to meet with the dragons…)"
    menu:
        "Call for Cyril.":
            jump meet_dragons
        "Explore on your own.":
            jump explore 

label ignore:
    p "..."
    c "Oh yes.  Oh of course, there is an apparition in front of me, oh Cyril.  You’ve finally done it.  You’ve gone completely bonkers."
    "(He thinks I’m a ghost?! What a strange man... still, I can use that to my advantage and slip past him)"
    c "Well, back to that spell again.  Biggeldy- I'll never get it!  Now where did I keep that spell-book.  It was around here somewhere!  "
    c "I just need to find it.  Perhaps one of those surly old dragons know where it got to."    
    "(Yes! Lead me right to the dragons!  I’ll just follow from a discreet distance…)"  
    
    c "Dragons.  I do need to ask you about my spell book. It seems I've misplaced it."
    c "Again."
    n "Cyril the Cowardly."
    n "And I see you've brought us a tassssty morssssel.  How generous."
    c "Oh don’t mind her.  She’s just my apparition.  Wait.  Why can you see her?"
    # TODO: Finish this branch or make it join in with the main. Early ending?

label meet_dragons:
    c "Well, it's time to meet the dragons.  I must warn you, do not believe a word they say.  They can be quite cutting at times.  I remember this one day where they- well that's not important and I most certainly did not cry for days about it."
    c "The dragons are Niir and Balrung?  Niir, well, don't be surprised if he looks at you like he might eat you for dinner.  He quite looks at every female that way.  It is a good thing that I am not a female sometimes because it is rather disconcerting to be approached like a piece of meat.  Balrung, he is much more courteous but he is rather stubborn.  He will try to make you see it his way and not by the most honest methods."
    p "Interesting...well, lead on."
    c "Ah, yes.  Now where did I keep that key.  It is a magic key and it should be... yes.  There it is, right in the stone there.  Accimeidum! Now we shall enter."
    c "Helllo!  Dragons!  It is I, Cyril.  Are you in here?"
    b "Merlonious. Here to taunt us again? Yes, dangling the key in front of the chained prisoners, very tasteful. But who’s this charming lady?"
    n "I sssssee that you have brought a friend.  Delic-delightful."
    c "Oh no you don't.  This is royalty.  A royal princess and I will not have you looking at her like that Niir.  I mean, I don't- I can't- Regardless, she is here to see you.  Apparently.  Though I still don't get why..."
    menu:
        "Allude to your purpose in veiled terms.":
            $ balrung_affection += 1
            p "I, Princess [name], am here in the hopes that one day, old enemies may become allies who work together to remedy the injustices of the realm."
            n "I would rather work on the injustices of that unflattering dress of yours.  How about you come a little closssser, so that I can see it more fully." 
            b "There are many injustices I would fight, had I only the freedom to do so."
            c "Now, now.  Behave, you two."
            
        "Pretend you are just checking on things.":
            p "I’m Princess [name]. I just… wanted to see how things were going here. You aren’t being mistreated, are you?"
            b "Well, would you call it mistreatment to keep someone chained not only to a location, but inside an inferior form? This frail human-like appearance is not our normal state, you know."
            c "Oh, he's just being dramatic Princess.  They know the rules of the agreement.  They can leave once they find love and find reform.  True reform cannot happen without love, you know.  So they are quite simply prisoners of their own choosing."
            n "I would call it mistreatment to be kept away from such a beautiful sight daily -to see the sights and smell the wome- flowers.  It has been unfortunate.  Perhapssss you are here to help though?  Eassse the pain?"
    
    # Whom to talk to?
    menu:
        "Address Niir.":

            p "Niir...what an interesting name. Tell me about yourself."
            n "Intrigue you do I?  I ssssuppose I would.  Unlike my decrepit friend here who has no sense for amusement or play.  How about you, are you interesssted in fun?  Perhaps playing a little game?"
            p "Tell me what it is, and then I shall decide."
            n "Oh, it is a game that would have you sssscreaming for more.  That much is for sssure.  To be up here in this castle tower you are obviousssly not afraid of heights.  Perhaps you would like to get higher ssstill?"
            p "What did you have in mind?"
            n "That, is my little sssecret.  You will have to help me leave to find out."
            
            menu:
                "\"I shall consider your... offer, Niir.\"":
                    $ niir_affection += 1
                    p "I shall consider your... offer, Niir."
                    n "I’ll be waiting.  Until then, why not come clossser?  Let usss get… acquainted."
                
                "\"I’m through with you.\"":                    
                    p "I’m through with you."
                    n "Pity.  I could have a lot of ussse for someone like you as my plaything."
                    b "This Princess is no one’s ‘plaything’, Niir, least of all yours. But, Princess, tell us about yourself. How is the royal family?"
                    n "You have no ssssense of fun.  But if you would rather spend time with thisss sssourpus, then you can make your choice."
                    p "My...family? (not sure what to write here)"

        "Address Balrung.":
            $ balrung_affection += 1
            p "Balrung...how long have you been here?"
            b "Forty years, by human reckoning. And even though that is but a short time to a long-lived dragon, since we are imprisoned within human form we feel every second of our captivity keenly."
            b "Well, I do, at any rate. I’m not sure I can say the same for my heartless young...companion here."
            # TODO: Have Niir doing something funny, oblivious that he is being talked about?
        
        "Address Cyril.":
            $ cyril_affection += 1
            p "It’s just these two? Aren’t there any other dragons here?"
            c "Well, as I said.  Most of the other dragons have moved on.  Actually, come to think of it, I've forgotten when the last one left.  Who was that heroine who came to- Or maybe it was some wilderbeast.  "
            c "I'm not even sure if I'm remembering it right.  But these two have made this place home for a long time."
            p "You must have considerable magical powers, if you are guarding them here all on your own."
            c "Oh, well I wouldn’t say.  I mean people have said.  Well, my mother.  Once.  But yes, I suppose someone has to do the job and that someone is me.  It’s quite a funny story really, I just fell into it.  "
            c "I was at the council and they were all concerned about the legacy of my master and they were all shouting over one another and didn’t even realize I was in the room.  "
            c "And I was telling them all that something must be done about those pesky dragons…"
            c "And then they all left.  And put out the lamps and I was just there.  So I guess the council had made their decision after all, that I was to do something about the dragons.  And here I am."

    # After talked to Niir, Balrung, or Cyril
    c "So there we have it.  The dragons.  As you can see my job is not at all easy."
    c "I don't want to dwell on it but there have been some times where I have just felt like giving up!"
    p "You don't say."
    c "But regardless you are here now, your majesty, so it isn't all bad!  Not at all."
    c "Food is pretty spare in these parts, thanks to how isolated everything is."
    c "I normally conjure something up, however."
    c "If you'd like, you could join me for a supper.  Otherwise I could bring something to your room?"

    menu:
        "\"I'd rather have something brought to me, and brought to me hot!\"":
            jump broughtfood
        "\"I suppose I could join you if you don't bore with with your stories.\"":
            jump joinmage 

label joinmage:
    $ cyril_affection += 1
    c "Ah, yes Princess.  So glad of you to join me."
    c "I mean glad of me."
    c "I mean I'm the one who's glad."
    c "I'm terribly sorry, I don't seem to be making much sense."
    p "It's Moronious, isn't it?"
    c "Merlonious.  Cyril Merlonious."
    p "Have you ever thought of changing your name to Moronious?"
    c "Why would I do something like that?"
    p "Why not?"
    c "Yes, erm.  Good point."
    c "I'll just whip something up for us.  But nothing too complicated."
    c "Actually, my repertoire isn't that vast with food spells."
    c "So I'd better just do what I can do."
    "..."
    c "I hope it is to your liking."
    c "It's not much but I-"
    p "Silence."
    c "Ah, yes.  I will be entirely, completely-"
    c "Silent."
    
    
    
    c "Yes, well, I was given the name Merlonious after the great Merlin, you see."
    c "But I guess, to family I've always been Cyril.  Cyril the Competent, they say."
    c "Which actually isn't much of a compliment come to think of it."
    c "But never mind that."
    c "Are you enjoying your meal?"
    p "You do know that I am a princess, correct?"
    p "And in what way did you think that this was worthy of a princess?"
    c "I... I'm not quite sure."
    
    
    ## MAGE ROUTE

    
    
    
label mage_time4:
    c "Ah, yes.  Princess."
    c "Have you ever had one of those days?"
    p "One of... those days?"
    c "The days when nothing seems to go right."
    c "I honestly felt like everything was coming together and then-"
    c "Alekaadoo!  Everything goes topsy turvy."
    p "Is this to do with dragons stealing your spellbook again?"
    c "Oh?  You think they stole it?"
    p "Is the sky blue?"
    c "Ah.  A riddle!  I am quite fond of riddles."
    p "No, it was sarca- you know, never mind."
    c "But not on a day like today."
    c "On a day like today I would much rather hide my head in my hat."
    p "Perhaps you're feeling miserable enough to, I don't know, {i}release the dragons?{/i}"
    c "Oh no.  I'm not quite miserable enough for that."
    p "Well, what can we do to make you {i}more{/i} miserable then?"
    c "Hmmm... I guess if I am to be reminded of my childhood I will probably be more miserable."
    p "{i}Your{/i} childhood mage?  What was so wrong with {i}your{/i} childhood?"
    c "I learned all my spells quite well, but I was rather ignored for the flashier mages."
    c "People didn't really remember my name and my own mother told me to stop snivelling about being forgotten."
    c "Even though it was in private, and I can do what I like with my private time and..."
    p "I've heard enough."
    c "Y-ou have?"
    p "Yes, I have and this is pitiful.  I mean, do you have any comprehension of what life was like growing up in the royal castle?"
    p "{i}Do{/i} you?"
    p "Everyone doing your bidding and acting all sweet and kind to you just because!"
    c "Ah, yes.  That does-that does sound horrible."
    p "It was monsterous, hidious.  And my sister, she always got complimented first - {i}first!{/i}"
    p "I mean, it's not as though I'm second rate.  So why her?"
    c "Well, she is the elder out of you... so I'm sure it was just-"
    p "If I want your opinion I'll ask."
    c "I'm sorry you had such a dreadful time."
    c "But you are here now, and I am more than willing to do anything to appease you, your majesty."
    p "I will take you up on that."
    
    
label mage_time5:
    p "You really are quite pathetic, aren't you?"
    c "Ex-excuse me?"
    p "I mean, no one knows who you are.  You're guarding this tower with no reward."
    p "You're completely pathetic."
    c "I-I... I assure you that I'm not."
    c "Surely, some people have said some things akin to that, but they d-do not know."
    p "You assure me?  How inspiring.  So I should believe you then?"
    p "Is it not true that you cannot do a thing here?"
    c "I am loyal.  I did not have to take up post here."
    p "And where has your loyalty got you?  Hmmm?"
    "His eyes flashed dangerously."
    "(What do you know?  There is something boiling under that bumbling facade.)"
    c "You are testing me, Princess."
    "(And I'd never had so much fun.)"
    c "What are you doing, your majesty?"
    p "Taking your wand, of course."
    p "You don't really need it, do you?"
    c "I do... need it.  Most certainly."
    p "Beg me."
    c "Um- pardon?"
    p "Beg me for it."
    "(He is not proving himself in the slightest.)"
    "(But still it is amusing... perhaps he could make a good {i}slave{/i} one day...)"
    c "I will not."
    p "Of course you will, you're pathetic and I can do whatever I lik-"
    c "You {b}will not{/b}."
    "(Is that lightning?)"
    "(Cyril the Chaste has {i}actually{/i} beoome scary.)"
    p "Fine.  Have your wand."
    "(Perhaps he is worth more than a slave after all)."
    
    
    
label mage_time6:
    p "Merlonious!"
    c "It's actually.  Yes, Merlonious.  That is my name."
    p "Well, I am glad that I caught you."
    p "It seems that I am rethinking your uses."
    c "Oh, erm... thank you?"
    p "Yes.  My future kingdom may have a place for you."
    p "I'm sure we could come to some arrangement."
    "I reached out to touch him on the shoulder."
    "And he recoiled quickly, much to my amusement."
    p "You have never been touched by a woman before, have you?"
    c "Errr, yes.  I mean no.  Not entirely in person, no.  But I have watched the dragons and read some rather riveting books.  But short answer… erm, no."
    p "I should have guessed."
    
label mage_insane:
    b "It took only a few short years of solitude to lose your mind."
    b "Are you sure she's even real?"
    m "Yes!  Of course I am!"
    n "Sssshe's interested in you.  Ssshe must not be real."
    m "She is real.  She is the real princess.  Just look at her."
    b "Are you sure about that?"
    n "I can't ssssee a thing."
    p "You blithering fool, Cyril.  They're playing you."
    p "Of course I'm real."
    b "Exactly what a false princess would say, don't you think?"
    n "Exacccctly."
    p "Cyril the Clueless.  You astound me.  I came here for a dragon."
    p "But despite your many inadequacies - and there are many - I found myself drawn to you."
    m "I do find it highly unlikely that an apparition would call me inadequate and clueless."
    b "Unless you were making her up to be realistic."
    m "I am!  I am!  So true!  I just wanted it to be true!"
    "(Is he for real?)"
    p "Oh for the love of..."
    menu:
        "Kiss him.":
            jump mage_insane_kiss
        "Step on his toes.":
            jump mage_insane_step
            
label mage_insane_kiss:
    "..."
    m "Ah, sweet, sweet apparition."
    m "I'm afraid this is the closest that we're going to get to being together for real."
    p "Cyril the Crazy, I just kissed you."
    m "And I'm going to spend all my years in this castle imagining you."
    p "You are completely insane."
    m "Insane with love, my dear."
    p "No, insane with insanity.  I'm leaving."
    m "But you can never leave, as you are in my mind."
    p "Watch me."
    p "Dragons, sorry it didn't work out."
    p "Cyril, this has been a complete waste of my time adieu."
    
    #MAGE INSANE END
    
    
label mage_insane_step:
    m "Ouch!  You trod on me!"
    p "Would an imaginary person do this?" with hpunch
    p "Or this?" with hpunch
    m "Ow!  Ow!  Ow!"
    m "I suppose not.  You must be real after all."
    p "Yes and I was hoping that a certain foolish mage and I might go to the council of mages to get someone else to do this job."
    p "It seems I'm going to need you in the immediate future."
    m "I'm yours my majesty, I mean {i}your{/i} majesty of course."
    p "You had it right the first time."
    