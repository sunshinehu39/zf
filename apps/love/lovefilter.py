from django import template
register = template.Library()

import datetime

# 自定义过滤器：年份计算年龄
@register.filter
def age(birthyear):
    return datetime.datetime.now().year-birthyear


# 自定义过滤器：女-星座解读
@register.filter
def star_signs_girl(constellation):
    signs = ''
    if constellation=='白羊座': signs='豪放率真的白羊座女生，富有强大的想象力，热情勇敢，女汉子味十足。勇往直前，是你们最大的特点。所以即便面对困难挫折，白羊女都敢于迎接挑战。可以说，这是个极具战斗精神的新时代女性。如此强悍个性的白羊女，在异性的眼中却永远都少了点女人味专属的温柔，往往都是称兄道弟的份。'

    elif constellation=='金牛座': signs='八面玲珑的金牛座女生，恰到好处的交际手腕总能赢得众人的好感。以金牛女勤俭节约的内敛个性，必然会是个模范的家庭主妇。只是深沉的事业野心，往往督促金牛成为精明能干的女强人。富有女性魅力的金牛女，兢兢业业的工作态度，虽然大器晚成，不过你们的坚韧会是成功中佼佼者。所以，金牛女大多都是晚婚者。'

    elif constellation=='双子座': signs='聪明伶俐的双子座女生，爱耍小聪明之余还有点神经质。抱有积极向上生活态度的双子女，内心闪耀着众多美好的幻想，以及充满了对理想的憧憬。可以说，这是个具有异国风情的魅力女生。你们的适应能力非常顽强，所以总能在张弛有度的生活、工作和爱情中，享受着无忧无虑的曲调。'

    elif constellation=='巨蟹座': signs='温顺随和的巨蟹座女生，充满着天真而感性的幻想。感情细腻的巨蟹女，注定是个多愁善感的悲情人。正因为敏感的神经线，才会日积月累了那么多忧怨不满的情绪。不过所幸的是巨蟹女思想单纯，心态永远都处于年轻的状态。只要别人的信任，就会散发出温情幽默的气息，简单而知足。'

    elif constellation=='狮子座': signs='光芒四射的狮子座女生，无论言行举止都流露着绚烂的戏剧性色彩。慷慨大方是狮子女的天性，你们就是喜欢追求生活中最顶尖的极品，唯有这种昂贵且高品位的东西才配得到“宠幸”。同样是事业型女强人的范，狮子女却是天生的领导者，拥有杰出的才能，以及做大事的度量。女生中绝无仅有的“王者”！'

    elif constellation=='处女座': signs='表面看似波澜不惊的处女座女生，其实内里隐藏着一颗敏感而躁动的心。内敛而保守的个性，使得处女女总是一副腼腆害羞的邻家女生模样。沉着冷静是你们的处事态度，正因为细致的心才需要更多的安全感，所以往往都是有所保留。对于生活，处女女需要强而有力的掌控感！'

    elif constellation=='天秤座': signs='高贵优雅的天秤座女生，富有极强的创造力。天生追求“美感”的天秤女，本来就是美的化身，拥有着天使的面孔魔鬼的身材。你们就是典型的外貌协会会员，注重外表之余往往会弱化看人的能力。就算是生活中再平凡的小事，天秤女都能将其幻化得奇妙无穷！天秤女，就是这样美感特佳的魅力女性！'

    elif constellation=='天蝎座': signs='谜样般的天蝎座女生，外表冷若冰霜，内在狂热不羁。让人捉摸不透的天蝎女，有着复杂而强烈的情绪。看似安静内敛的天蝎女，却具有狂野性感的挑逗力，对于男生来说那时无法抗拒的魅力。而且这是个敢爱敢恨的星座，你们更偏恋灵魂伴侣，一旦爱上就是“不成功便成仁”的壮烈追求。'

    elif constellation=='射手座': signs='极具挑战欲望的射手座女生，认为生活就是一系列的探险，尤其偏爱新奇刺激的经验。热情奔放的射手女，热爱自由，并坚定的认为一切皆有可能。射手女渴望生活充满变化和刺激，特别喜欢跟各种各样的人相处。而且射手女这种放浪不羁的个性，反而激发更多异性的征服欲，所以身边不乏狂蜂浪蝶。'

    elif constellation=='摩羯座': signs='保守固执的摩羯座女生，富有正义感，总是一副“路见不平拔刀相助”的侠义心肠。摩羯女不善言辞但贵在够真，所有的喜怒哀乐都写在脸上。个性略为强势，具有高度的责任感，摩羯女就是这样外柔内刚的人。不过缺少了点浪漫色彩，极端现实的你们，终身都在为着实现目标而努力，连做梦都与现实有关。'

    elif constellation=='水瓶座': signs='好奇心异常旺盛的水瓶女，是个反对世俗且不随波逐流的个性女生。极具独立精神的你们，喜欢我行我素的自由，说着自己的话走着自己的路，任由他人怎么说。在女生中，水瓶属于另外的理性份子，所有的聪明才智都用于天马行空的想象力。极端，纯洁，以及理智，便是真实的水瓶女！'

    elif constellation=='双鱼座': signs='柔情似水的双鱼座女生，天生浪漫且富有幻想，对众多男生来说有着一种特别的魅力。天真可爱，是大多数双鱼女的评价标签。或许正因为这样让人怜爱的个性，往往是异性朋友圈中的小公主。对生活，双鱼女充满着积极向上的热情，只是缺少了点应变能力，需要别人的保护，并习惯依赖他人。'

    return signs

# 自定义过滤器：女-星座链接
@register.filter
def star_url_girl(constellation):
    url = ''
    if constellation=='白羊座': url='http://www.xzw.com/astro/1/9658.html'
    elif constellation=='金牛座': url='https://m.xzw.com/astro/1/9658_2.html'
    elif constellation=='双子座': url='http://www.xzw.com/astro/1/9658_3.html'
    elif constellation=='巨蟹座': url='http://www.xzw.com/astro/1/9658_4.html'
    elif constellation=='狮子座': url='http://www.xzw.com/astro/1/9658_5.html'
    elif constellation=='处女座': url='http://www.xzw.com/astro/1/9658_6.html'
    elif constellation=='天秤座': url='http://www.xzw.com/astro/1/9665.html'
    elif constellation=='天蝎座': url='http://www.xzw.com/astro/1/9665_2.html'
    elif constellation=='射手座': url='http://www.xzw.com/astro/1/9665_3.html'
    elif constellation=='摩羯座': url='http://www.xzw.com/astro/1/9665_4.html'
    elif constellation=='水瓶座': url='http://www.xzw.com/astro/1/9665_5.html'
    elif constellation=='双鱼座': url='http://www.xzw.com/astro/1/9665_6.html'
    return url

# 自定义过滤器：男-星座链接
@register.filter
def star_url_boy(constellation):
    url = ''
    if constellation=='白羊座': url='http://www.xzw.com/astro/1/9631.html'
    elif constellation=='金牛座': url='https://m.xzw.com/astro/1/9631_2.html'
    elif constellation=='双子座': url='http://www.xzw.com/astro/1/9631_3.html'
    elif constellation=='巨蟹座': url='http://www.xzw.com/astro/1/9631_4.html'
    elif constellation=='狮子座': url='http://www.xzw.com/astro/1/9631_5.html'
    elif constellation=='处女座': url='http://www.xzw.com/astro/1/9631_6.html'
    elif constellation=='天秤座': url='http://www.xzw.com/astro/1/9649.html'
    elif constellation=='天蝎座': url='http://www.xzw.com/astro/1/9649_2.html'
    elif constellation=='射手座': url='http://www.xzw.com/astro/1/9649_3.html'
    elif constellation=='摩羯座': url='http://www.xzw.com/astro/1/9649_4.html'
    elif constellation=='水瓶座': url='http://www.xzw.com/astro/1/9649_5.html'
    elif constellation=='双鱼座': url='http://www.xzw.com/astro/1/9649_6.html'
    return url

# 自定义过滤器：男-星座解读
@register.filter
def star_signs_boy(constellation):
    signs = ''
    if constellation=='白羊座': signs='满腔热情的白羊男，总是一副无畏无惧的“超人”模样。在白羊男的字典中根本就没有“放弃”、“失败”等负面字眼，所以他们总能迎难而上，并表现出压倒一切的正能量。直白不含蓄，技能是速战速决，长驱直入！'

    elif constellation=='金牛座': signs='性格保守且沉稳的金牛座男生，如同归隐诗人般追求安稳恬静的田园生活。其生活节奏趋于缓慢且有条有序，你们不希望任何人扰乱自己的步伐节奏。不管是物质还是感情，现实主义的你们总是以“可靠”作为自己一切的衡量标准。'

    elif constellation=='双子座': signs='好奇心旺盛的双子座男生，对周围一切新奇刺激的玩意都充满着无止境的探索欲望。跟金牛相反，你们更乐于接受瞬息万变的生活节奏。所以双子男是极具意象色彩的人，总是在某个角落弹奏着恰好好处的弦律。在欣赏缤纷生活的同时，也不断吸引着新的“听众”。'

    elif constellation=='巨蟹座': signs='巨蟹座男生向来低调，个性温顺亲和，平易近人，举止稳重。众人都称赞巨蟹男温情顾家，心地善良。平日深居简出的巨蟹男，虽然其主要的领地是“家庭”，但事业上也是有着独树一帜的表现。只是在面对已认定的问题上，巨蟹男则略显固执，甚至会顽强抵制。'

    elif constellation=='狮子座': signs='极具个性的狮子座男生，拥有着异于常人的能耐和韧性。这也是你们被成功之神眷顾的原因之一。自信且有主见的狮子男，有着卓越的领导才能，不仅威信十足，而且身边不乏追随者。反过来，你们却受不得被命令，凡事以自我为中心。如此自尊自傲的狮子男，其实内心孤独脆弱，只是用冷峻的外表掩盖了而已。'

    elif constellation=='处女座': signs='聪慧理智的处女座男生，如同女生一样拥有着细腻如丝的情感和思绪。做事按部就班的处女男，是个典型的完美主义者，这已经是家喻户晓的事实。或许过分要求完美，导致性格上略显婆妈，待人过于严苛，挑剔成性。然而这种一丝不苟的态度，往往能够让你们在工作上取得骄人的成就。'

    elif constellation=='天秤座': signs='极具人格魅力的天秤座男生，在异性心目中是理想的伴侣。温柔尔雅且举止大方的天秤男，天生就具有交际高手的魅力，能说会道的你们在任何场合都深得别人的欢心。你们以追求“美感”为原则，凡事都要求做得尽善尽美。虽然你们是体贴入微的好恋人，但过分讨好的异性缘却难免有朝三暮四的嫌疑。'

    elif constellation=='天蝎座': signs='高冷的天蝎座男生，性格属于思辨型，拥有着高度敏锐的洞察力。凛然正气的天蝎男，对外界的戒备心非常强，只要有风水草动会就马上警惕。虽然个性争强好胜，但你们却能崇尚公平的竞争精神。得益于冷静的判断力，天蝎男极少会吃亏，难得的是不怕吃亏。因为你们展望的可是未来的谋划，而非眼前的小利。'

    elif constellation=='射手座': signs='风趣幽默的射手座男生，个性爽朗而机敏，给人的印象就是典型的阳光大男孩。达观的射手男还是社交高手，特别能讨女生们芳心，往往是大众情人的角色。从来不知愁滋味的射手男，总能把欢声笑语带到每个场合。如此懂得享受生活的射手，追求自由，来无踪去无影如同风一样的男子！'

    elif constellation=='摩羯座': signs='成熟稳重的摩羯座男生，具有让人五体投地的不屈不饶精神和能耐。摩羯男总是理性先行，天生冷静的判断力是你们成功的秘诀之一，往往都是白手起家的模范。虽然你们拥有着高度的责任感，但却永远都缺乏点灵活性，不擅长速战。摩羯男习惯固执且谨慎地坚持认定的事，所以也经常与机会擦身而过。'

    elif constellation=='水瓶座': signs='外表朴实爽朗的水瓶座男生，内里是个错综复杂的人，如同一本厚实的字典让人难以读懂。热情率直且乐于助人的水瓶男，有时候却会表现出不近人情的冷漠一面。你们从来不受约束，只管走着自己的路，让别人去说。崇尚自由的水瓶男，极具个性且富有魅力，徘徊在矛盾和悖论的边缘。'

    elif constellation=='双鱼座': signs='温柔多情的双鱼座男生，就是一典型的风流才子范。双鱼男充满了浪漫唯美的色彩，在你们的世界里拥有着对爱情美好得如童话般的追求。之于生活，双鱼男却知足常乐，只要得过且过即可。看似文弱不堪一击的双鱼男，面对困难险阻时却能迸发出惊人的不服输精神。只是在抉择面前，却又显得特别黔驴技穷。'

    return signs
