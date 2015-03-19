label day2:
    scene bg bedroom day with fade
    "Is that knocking?! Who could be brazen enough to wake me up so early?!"
    p "Niir! I am in no mood for your games! Begone!"
    c "Please, Princess, it is I, Cyril, and I only wanted to-"
    p "Moronious?! This had better be important!"
    show cyril hat neutral at center with moveinleft
    c "Good.  Good.  I'm glad that you opened up."
    c hat concerned blush "I don't want you to think that I'm - well, disapproving."
    c "But some information has come to my attention."
    c hat concerned blush eyes closed "You were {b}banished{/b}, Princess!"
    p "I am well aware of that.  So what are you bothering me for?"
    c hat surprised "It's just- you were {b}banished{/b}, Princess!"
    p "If you're going to waste my time like a stuttering fool Moronious, I suggest you begone!"
    c hat smile "Well, it wouldn't be the first time that you've commanded me to begone."
    c hat concerned "Anyway, please tell me this is a mistake!  It must be a mistake!"
    c "I'm sure that the kingdom is just overreacting.  Playing a joke perhaps? Like Niir?"
    c hat concerned eyes closed "There is no way they would actually b-b-banish you!"
    p "Oh, they did banish me.  And that's why I'm here, to get justice."
    p "And {b}you{/b} will be part of those plans."
    c hat surprised "Erm-ahem!  Yes.  I don't think that is a good idea- it is already dangerous enough to have a disgraced Princess-"
    p "You don't {b}want{/b} me here?"
    "Who does he think he is?  I'm not the one at fault here!  I'd like to {b}see{/b} him try to kick me out!"
    c hat concerned blush "No! I didn't say that."
    c hat concerned "I'm just {i}concerned{/i} Princess."
    c hat concerned eyes closed "If you have serious allegations before you then ah-"
    p "You're ashamed of me being in your presence, then?"
    c hat concerned blush "No!  I love you being in my presence."
    c hat concerned blush eyes closed "{i}I do{/i}.  It's just..."
    c hat concerned "I'm afraid for you and the errr... connotations that are attached to that."
    p "I can handle myself Moronious."
    p "And when I put things right you will see that for yourself."
    c hat neutral "As long as I'm not seen as {i}aiding and abetting{/i}."
    p "If you are not willing to make sacrifices for your future Queen, then what good are you?"
    c hat concerned blush "I am, I am.  Forgive me your highness."
    p "I forgive you, you foolish mage.  Just don't doubt me again."
    p "Oh, and one more thing."
    c hat surprised "Yes, highness?"
    p "You will join me for dinner in the kitchens. Tonight."
    c hat concerned blush eyes closed "Y-yes, of course!"
    hide cyril with moveoutleft
    
    show niir neutral at right with moveinright
    n "You were banisshhed? Your position musst be desssperate, then."
    p "How long have you been eavesdropping?!"
    n "Long enough to hear you sssnorrrring. Mossst unladylike."
    p "Moronious!"
    show cyril hat neutral at midleft with moveinleft
    c hat surprised "Yes, Princess? Oh! What's {b}he{/b} doing here?!"
    p "That was my question. I would have thought that a capable mage would have this room warded against unwanted intrusions."
    n "If you think Cccyril is capable--"
    c hat concerned "I did! It was! But- oh, the spell's locus...I had it tied to me, not the room! What a dreadful oversight."
    c hat concerned blush "I am terribly, terribly sorry, Princess! I shudder to think what these terrible dragons might have tried to do if I had not fixed the ward."
    p "Yes, well, it should have been fixed in the first place!"
    n "Disssapointing. I had ssso many plansss..."
    c hat neutral "Now I've made two spells - one tied to you, and one to the room. The locus for the room spell is the door, so if you open the door, the spell will allow people through."
    c hat concerned "I've also added a spell on your person, that creates an anti-dragon barrier. I don't know why I didn't do this in the first place, it must have slipped my mind."
    n "Like ssso many other thingsss."
    p "So dragons cannot touch me now? What would happen if they tried?"
    c hat smile "They can only touch you if you reach out to touch them first. As for what would happen... ahem! Let's just say they would regret such an action!"
    p "Hmm. What a powerful spell. Would you like to test it, Niir?"
    n "I have tesssted that ssspell before. I have no desssire to experrrience it again."
    p "I see. Thank you, Moronious; you may go."
    c hat concerned blush "P-princess, I don't think it's wise to be alone with this, this..."
    p "Do you not trust your own spell? Or is it {b}I{/b} you do not trust?"
    c hat concerned blush eyes closed "No...I trust you, just- please, be careful!"
    hide cyril with moveoutleft
    
    p "Do you have business with me, dragon?"
    n "Yesss, Balrung wished to ssspeak with you."
    p "Well, where is he? Why doesn't he just come knock on my door?"
    n "I think he jussst likesss to send me on errandsss."
    p "So, you weren't really watching me sleep for hours...?"
    n "I'll let you wonderrr about that one."
    p "Hmph. I won't be losing sleep over it. But, as long as you're here..."
    n "Yesss?"
    p "Join me for dinner tonight. In the kitchen."
    n "I'll be therrre."
    hide niir with moveoutright
    
    p "I suppose I'll see what Balrung wants..."
    if (asked_scepter == "Balrung"):
        "Perhaps he has found the scepter?!"
        
    scene bg dungeon with fade
    show balrung neutral at center with dissolve
    p "Balrung! I don't appreciate being summoned to meet with {b}you{/b}! Next time you will come and meet with me!"
    b smile "My apologies, my lady, I didn't think it appropriate to disturb a lady in her bedchamber so early in the morning."
    p "But you thought it appropriate to send the lascivious Niir to my bedchamber?!"
    b smirk "I did not send him. I merely mentioned that I hoped I would get a chance to talk with you today, and he departed."
    if (asked_scepter == "Balrung"):
        p "Well, what is it? Have you found the scepter?"
        b determined "No. It seems to be somewhere nearby, but I cannot discern its exact location yet."
    else:
        p "Well, here I am. Speak."
    
    b neutral "I understand you are not here entirely of your own free will. That you were banished."
    p "A temporary state of affairs, I assure you."
    b determined "Believe me, Princess, when I say that I understand completely. I know all too well how it feels to make one lapse in judgement, and have inordinate punishment dealt to you."
    p "You... understand?"
    b angry "Those who fear power are often overly vindictive against those who use it."
    p "Vindictive, yes. Have you met my sister, Magnolia?"
    b determined "No, but I knew someone quite like her, once. Afraid of my power."
    p "Self-righteous."
    b angry "Ambitious."
    p "Narcissistic."
    b determined "Self-sacrificing."
    p "Knows whats best for everyone else."
    b neutral "Yes, precisely. So if you are in need of allies here, I hope you will seek me out, and perhaps we can aid each other."
    p "But you could only aid me if you were freed."
    b smile "Well, I would certainly have much greater power as a free dragon. But I am willing to do what little I can for you, in this form, as well."
    p "I shall consider your offer, dragon."
    b smirk "Please do."
    p "But first, I have a simple request of you."
    b neutral "Yes?"
    p "Come to the kitchen at dinner time and eat with me."
    b smile "I'd be honored, Highness."
    scene black with fade
    "And now, for dinner...A little test, to see who would be the most useful to me..."
    
label dinner_party:
        
    scene bg kitchen with fade
    show niir neutral at right
    show balrung neutral at center
    show cyril neutral hat at left
    with dissolve

    p "Good, you are all here. That proves you can fulfill a simple request."
    b smirk "It has been a long time since I attended a dinner party."
    n "I hope the food issss better than usssual."
    p "Yes, a dinner party requires food. Moronious? Isn't that your job?"
    c hat surprised "R-right! But, surely you, you don't want to eat with these...creatures?"
    n smile "She sssssummoned usss here.  Sssso clearly sshe doesss."
    p "Yes, yes.  What that Niir dragon said.  I need all of you present."
    c hat concerned "I just thought that when you requested dinner-"
    b smile "You assumed she wanted be alone, with you, over a candlelit dinner? That's rather presumptuous, Merlonious."
    n mischief "Hilarioussss, don’t you think?"
    c hat concerned blush "That wasn’t- it wasn’t entirely like that.  You must believe me Princess."
    show cyril neutral hat at left
    p "I don’t care what you thought.  Your future Queen hasn’t the time to consider such things.  What a waste.  No, I thought it would be nice for us to...{i}talk{/i} together about matters of the kingdom."
    p "{b}Food{/b}, Moronious!"
    c hat neutral "Right on it!  I apologize your majesty."
    c hat angry "Vittus Cottura!"
    show cyril hat concerned with flash
    p "Honestly, not {b}that{/b} again Moronious.  Is that all you know how to summon?"
    c hat concerned "I’ll try something else then."
    n "We’re waitingggg."
    c hat concerned eyes closed "Do be quiet, dragon, you are making me lose my concentration."
    show cyril hat concerned with flash
    # TODO: magic vfx
    b angry "I am convinced that Merlonious summons this pitiful human food as part of our punishment. Dragons were never meant to be herbivorous."
    c hat concerned "I-it's good for you!"
    n "Ohhh, what I wouldn't give for a bit of deer, or mutton, or even ssssquirrel!"
    b neutral "Elk..."
    n "Turrrkey..."
    b "Bison..."
    n "Rrrrabbit!"
    c hat angry "Enough complaining, both of you."
    p "Yes, anyway, I brought you all here together in order to discuss something."
    p "It has come to my attention that all of you now know about my purported banishment." 
    c hat surprised "Purported?"
    p "Quiet, Moronious!  As I was saying... you all know the true reason why I am here.  And so, you all must realize by now that I have been cheated out of my destiny by my own blood."
    b smile "Destiny is an unfaithful mistress..."
    n "Desssstiny, you ssssay?"
    p "I'm sure you all realize that if you were to align with my sister, you would be no friend of [k_name].  So it would be wise of all of you to work out where your allegiance lies."
    n "Dragonsss have no allegiancccce." 
    b smirk "What advantages would an ally of yours gain, I wonder? And what would your sister do with this prison?"
    c hat surprised "No, no, no, no, no, no.  We cannot be talking about this, Princess.  These are political matters.  This is not up for discussion over dinner."
    p "Oh please, mage.  I think we’re all adults here.  Surely we can discuss the future of the kingdom together without any..."
    n "Or we could dissscusss other forbidden topicsssss..."
    b determined "That would be like the blind man describing a sunset in your case, Niir. No, let the Princess speak."
    c hat angry "I warn you, speaking of things like this never go well.  My, word might even get out that we’re {i}conspiring{/i}!  Conspiring, Princess!  I think it would be best if we leave this alone for the present moment."
    p "Charges of conspiracy only matter if we lose. No one charges Queens with conspiracy!"
    c hat concerned eyes closed "It’s not the charge itself.  It’s the principle.  I would rather not take part in such a discussion."
    b determined "Leave, then, and let the adults discuss matters too weighty for your simplistic morals."
    n "Ssssimplistic Cccyril.  What ssshall we do with you?"
    c hat concerned "I don’t think we need to do any-"
    show niir at quarterleft with quickmove
    show niir at right with quickmove
    c concerned blush "Excuse me, dragon!  Just what do you think you’re...."
    n "Hahahaha.  Oh, look at that.  Hissss faccce is red."
    c concerned "A hat is a rather serious piece of a magical wardrobe.  So I demand that you give that back."
    c concerned eyes closed "This instant, Niir!"
    n "Thissss inssstant, you sssay?"
    show niir at center
    show balrung neutral at right
    with move
    c angry "Don’t you dangle that thing in front of me, Niir.  This is no joking matter."
    c concerned "And no, I will not jump for it.  I will not sink to such standards."
    b smirk "Princess, it looks like you and I might need to discuss matters on our own, later, away from the squabbling children."
    p "Perhaps. For now, I shall simply enjoy the evening's entertainment."
    n "How about you fetch?  Insssstead of jumping."
    c angry "Don’t you dare throw that Ni-"
    show niir at quarterleft with quickmove
    show niir at center with quickmove
    c concerned eyes closed "He threw it.  Of course he did.  "
    c concerned "Stay right here dragons, while I come right back.  Please keep an eye on them Princess."
    hide cyril with moveoutleft
    "Oh, I'll keep an eye on them, alright. But, which one?"
    menu:
        "Talk to Balrung":
            $ balrung_affection += 1
            p "Balrung, you should know that my sister Magnolia is not a friend to dragons."
            b neutral "Why do you say that?"
            p "She's been trying to convince my father to sign new legislation forbidding dragons from holding titles." 
            b smirk "Are there many dragons attempting to hold titles?"
            p "Oh, yes, it's quite the craze to have a dragon consort. Princess Dianthus from two kingdoms over wanted to make hers King-Consort, but the United Council hasn't acquiesed yet."
            b determined "And what do you think they should do?"
            p "Human, dragon, I don't really care, as long as I'm the Queen!"
            b smile "Interesting."
            
            show cyril hat neutral at left with moveinleft
        "Flirt with Niir":
            $ niir_affection += 1
            p "Now that we have gotten rid of that {i}inconvenience{/i}, we can get back to business."
            p "I've enjoyed your antics; you are quite the asset to have on hand, Niir."
            n "I would like to have my handsss on your-"
            b smile "You were asking for that one, Princess."
            p "Of course I was. And Niir was kind enough to deliver."
            n "Kind?! You'rrrre suppossssed to be outraged!"
            p "Why would I be outraged when you said exactly what I predicted? That wouldn't be logical, would it?"
            b smirk "Oh ho ho! Careful with this one, Niir."
            n "Perhapssss I should try harder to sssurprise you."
            "That's exactly what I'm hoping for..."
            p "You can try, but I don’t believe it will be possible."
            n "Nexxxxt time, Princessss."
            show cyril hat neutral at left with moveinleft

        "Help Cyril":
            $ cyril_affection += 1
            scene bg stairs night with fade
            show cyril neutral at midright with dissolve
            p "Wait a moment, Moronious.  I’ll get that hat of yours."
            p "We wouldn’t want you to trip down the stairs doing so.  Actually, I’m not so sure that wasn’t what Niir had in mind."
            c concerned blush "Oh, thank you.  I’m most honored.  But I could not have you handling my hat yourself."
            p "And why not?  Is your hat too precious for mere royalty to touch?"
            c smile blush "Oh no.  That wasn’t what I meant at all.  It’s just, well, hats are a rather personal thing and I’m not sure if it would be strange suggesting-"
            p "Don’t be ridiculous, Moronious.  It’s only a hat."
            c laugh "Ah, yes.  You are right with that one.  Only a hat after all." 
            p "There it is."
            show cyril hat smile blush with dissolve
            c "I am most grateful."
            p "Do stop smiling like a nitwit.  Your desperate plea for pitying is starting to disgust me."
            show cyril hat neutral
            c hat concerned blush "Oh, of course.  I wouldn’t dream of disgusting you."
            c hat concerned "We should go back. I’m not sure what mess those dragons have gotten into already.  I dare say the food won’t still be there."

    p "Thank you all for an...informative evening. My apologies for the ineptitude of the chef."
    b smile "Thank {b}you{/b}, Princess. Your presence is a delightful change from the ordinary events of this wretched place."
    n "At leasssst the cccchef provided usss with entertainment."
    c hat angry "Nobody was impressed by that, Niir."
    p "So, we should get back to eating this horrid concoction that Moronious conjured."
    n "Disssgusting."
    c hat concerned blush "It is perfectly healthy and nutritious!"
    p "The things a princess must put up with for the future of her kingdom..."
    return