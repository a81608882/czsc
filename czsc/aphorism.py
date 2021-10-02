# -*- coding: utf-8 -*-
"""
author: zengbin93
email: zeng_bin8888@163.com
create_dt: 2021/9/25 13:38
describe: 摘录一些缠中说禅良言警句，希望能帮助更多人走出来。
"""
import random

texts = {
    "1": """
一定要注意，你不是多头也不是空头，但你一定要知道一旦发生什么情况，多头会干什么，空头会
干什么。例如，多头的愿望肯定是想补上面的缺口，这就构成市场的一个潜在力量，这个力量，在
其他力量的干扰下，可能一时发挥不出来，但这反而构成我们一个更好的买入点。请好好品味这句
话：你不当多头也不当空头，但一定要知道空头多头想干什么，而走势是最终的结果，他们想干的
是否干出来了，这才是关键。干不出来，有什么后果，他们会有什么后续的步骤，这才是该想的东
西。

--摘自《2008-01-29 15:19 年线支持初显现》""",

    "2": """
要战胜市场，首先要了解市场的众生。市场是合力的，而合这力的不是机械，而是活生生的人。市
场中，最多数的，都是糊涂蛋，赚钱了不知道为什么，亏钱了不知道为什么，最后变青蛙了，也会
说，井上面的天空好大，好复杂，怎么处理啊？哪里有拐杖啊？几乎绝大多数的人，进市场来时，
根本不知道市场是什么，然后就不断投入，最后有些输红眼了，砸锅卖铁也就进来了。对于市场，
本ID有一个观点，大概有点过分，但确实是对的。市场，就是要0投入去赚钱。

--摘自《2008-01-22 16:10 教你炒股票95：修炼自己》""",

    "3": """
要认清市场，首先要认清自己，知道自己的弱点在哪里，自己在市场中的每个行为，都要清楚地意
识到。每天收盘后，都找十分钟，把自己当天的操作以及看盘时的心理过程复一次盘，这是十分必
要的。

--摘自《2007-04-04 15:31 教你炒股票42：有些人是不适合参与市场的》""",

    "4": """
今天该股90%多的换手意味着，所有中签的人基本都抛了（对手盘包括其中），而且绝大多数都在
10几元抛的。这就对了，你们10几元不看好，有人要看好，市场向所有人开着，凭什么不能买？
市场就是一个斗心理的过程，大家都想一块去了，大家还用不用活了？

--摘自《2006-06-19 16:45 鄙视所有对N中工15元不敢买50元就吃醋的人！》""",

    "5": """
你的喜好，就是你的死亡陷阱！在市场中要生存，第一条就是在市场中要杜绝一切喜好。市场的诱
惑，永远就是通过你的喜好而陷你于死亡。市场中需要的是露水之缘而不是比翼之情，天长地久之
类的东西和市场无关。市场中唯一值得天长地久的就是赢钱，任何一个来市场的人，其目的就是赢
钱，任何与赢钱无关的都是废话。必须明白，任何让你买入一只股票的理由，并不是因为这股票如
何好或被忽悠得如何好，只是你企图通过买入而赢钱，能赢钱的股票就是好的，否则都是废话。因
此，市场中的任何喜好，都是把你引入迷途的陷阱，必须逐一看破，进而洗心革面，才能在市场上
生存。

--摘自《2006-06-09 17:03 教你炒股票3：你的喜好，你的死亡陷阱！》""",

    "6": """
能看清楚自己周围的市场陷阱，还只是第一步，更进一步，要学会利用市场陷阱来赢钱。当你要买
的时候，空头的陷阱就是你的最佳机会，当你要卖的时候，多头的陷阱当然就是你的天堂。这市场
，永远不缺卖在最低点，买在最高点的人，这世界上没有什么是可以让所有人赢钱的，连大牛市中
都有很多人要亏损累累。而市场中的行为，就如同一个修炼上乘武功的过程，最终能否成功，还是
要落实到每个人的智慧、秉性、天赋、勤奋上来！

--摘自《2006-06-09 17:03 教你炒股票3：你的喜好，你的死亡陷阱！》""",

    "7": """
市场是有规律的，但市场的规律并不是显而易见的，是需要严格的分析才能得到。更重要的是，市
场的规律是一种动态的，在不同级别合力作用下显示出来的规律，企图用些单纯的指标、波段、 
波浪、分型、周期等等预测、把握，只可能错陋百出。但只要把这动态的规律在当下的直观中把握
好、应用纯熟，踏准市场的节奏，并不是不可能的。

--摘自《2006-12-27 15:18 教你炒股票19：学习缠中说禅技术分析理论的关键》""",

    "8": """
战胜市场，其实就是战胜自己的贪婪、恐惧、愚蠢，本ID的理论只是把市场拔光给各位看，而拔光
一个人并不意味着就等于征服一个人，对于市场，其道理是一样的。不干，不可能征服市场。对于
市场来说，干就是一切。技术分析的最终意义不是去预测市场要干什么，而是市场正在干什么，是
一种当下的直观。在市场上所有的错误都是离开了这当下的直观，用想象、用情绪来代替。

--摘自《2006-12-27 15:18 教你炒股票19：学习缠中说禅技术分析理论的关键》""",

    "9": """
熟悉本ID所解《论语》的都知道，风险是“不患”的，是无位次的，任何妄求在投资中的绝对无风险，
都是痴心妄想。唯一的办法，就是设置一个系统，使得无位次、“不患”的风险在该系统中成为有位
次，“患”的系统，这是长期战胜市场的唯一方法。

--摘自《2006-12-01 12:03 教你炒股票12：一吻何能消魂？》""",

    "10": """
贪婪和恐惧，人的死穴，周末到了，请给自己一小时去找找自己！

--摘自《2007-01-26 15:03 罗杰斯，有种的和本ID来个PK》
""",

    "11": """
任何个人、阶级，其力量归根结底来自自己，无须期盼或感恩于所谓的救世主、大救星。所有救世
主、大救星都不过是人造的，连神都是人造的，没有造的人，即使是神，也什么都不是！    

--摘自《2006-04-23 18:32 鼓吹救世主、大救星的是真正的精神鸦片！》
""",

    "12": """
每一个人，都是天地不能覆盖，世界的风云雷电就在每个人脚下，自我憋屈只不过是去成就如大救
星般的无聊玩意。历史由每个人所创造，历史由每个人而命名，如果真有什么大救星，你就是你的
大救星！

--摘自《2006-04-19 21:42 布什，当今世界的大救星！》
""",

    "13": """
市场中没有人会同情你，当你哀求着股市跌时不要跌，楼市涨时不要涨，最终都不过成为了市场中
的炮灰。市场只有在所有能成为炮灰的都成为炮灰后，才会休息或改变方向。市场就是市场，市场
上的炮灰都是那些企图成为“大救星”或企图成为被“大救星”的人，而人类社会这个大市场也一样！

--摘自《2006-04-24 21:08 中国楼市股市的闹剧，都是“大救星”思维流毒所致！》
""",

    "14": """
操作其实很简单，一个基本的原则就是，任何走势，无论怎么折腾，都逃不出这个节奏，就是底、
顶以及连接两者的中间过程，因此，在两头的操作节奏就是中枢震荡，只是底的时候要先买后卖，
顶的时候要先卖后买，这样更安全点。至于中间的连接部分，就是持有，当然，对于空头走势，小
板凳就是一个最好的持有，一直持有到底部构造完成。而有技术的，根本就不需要什么小板凳，按
操作级别，分清楚目前是三阶段中的哪一段，然后日日是好日，时时是花时，不赚钱那真是脑子有
水了。亏钱都是错误操作引起的，不断反省，才会有进步的。

--摘自《2008-08-29 09:15 教你炒股票108：何谓底部？从月线看中期走势演化》
""",

    "15": """
底部都是分级别的，如果站在精确走势类型的角度，那么第一类买点出现后，直到该买点所引发的
中枢第一次走出第三类买卖点前，都可以看成底部构造的过程。只不过如果是第三类卖点先出现，
就意味着这底部构造失败了，反之，第三类买点意味着底部构造的最终完成并展开新的行情。当然
，顶部的情况，反过来定义就是。有了这个定义，就一定要搞明白，不是在底部的区间上买，而是
相反，应该和中枢震荡的操作一样，在区间下探失败时买，这才是最好的买点。

--摘自《2008-08-29 09:15 教你炒股票108：何谓底部？从月线看中期走势演化》
""",

    "16": """
牛人，一般是指站在潮流之巅的。在投资市场里，整体的失败是一次都不能发生的，只要发生一次
，基本就翻不了身了。个别的失败是允许的，但不能影响大局。

最早时几千万就可以当庄家了，现在几千万连大散户都算不上，在投资市场中，一次的跌倒，终生
都追不回来，基本只能在后面跟着玩了。而在后面跟着玩，怎么都算不了牛人。

--摘自《2006-11-20 12:00 教你炒股票8：投资如选面首，G点为中心，拒绝ED男！》评论
""",

    "17": """
意画心描自主奴，不管你相信与否，你的命运都是自己造成的，你的命运的改变也是自己造成的，
没有你自己种下的种子，佛也救不了你。有空，就好好看看你自己这个世界吧，看看自己曾种下什
么，又有什么正萌发，又有什么还在潜伏，又有什么被新种下了。善种子、恶种子，堆满你的世界。

--摘自《2008-01-20 21:01 刚到家，说两句》
""",

    "18": """
市场就如同一头牛，只有目无全牛，才可能随心解之而合其关节。在本ID的理论中，机械化操作
的本质就是目无全牛而合其关节，因为，根据本ID的理论，市场的结构已经被彻底分解，站在本
ID理论的角度，哪里有什么市场，不过是一堆的关节。而机械化操作，就是逐步合于其关节的节
奏，而不被全牛的繁复所影响。

--摘自《2008-04-13 21:51 教你炒股票105：远离聪明、机械操作》
""",

    "19": """
挣钱，本来就是很简单的事情，不过就是一个良好习惯与操作策略的结果，一点劲都不用费。那些
费力才能挣到的钱，也不会袋得住。

--摘自《2008-04-13 21:51 教你炒股票105：远离聪明、机械操作》
""",

    "20": """
股票这种面首，一定要控制成本，不要追高，有技术的，一定要通过震荡把成本往0甚至负处玩弄
下去，这才是玩弄股票之道。

--摘自《2007-07-09 15:35 中国股市前途的大决战》
""",

    "21": """
不要用你的想象代替现实。股市里的牛人每年都有，死去的牛人更多，市场的第一原则就是生存，
只要你30年后还能活下来，自然就是最大的牛人。

--摘自《2006-11-20 12:00 教你炒股票8：投资如选面首，G点为中心，拒绝ED男！》评论
""",

    "22": """
要长期胜利，就一定要坚持用最小风险换取最大利润，风险是第一的，这里没有什么高低之分。亏
损是按百分比的，一百亿和一百万，亏了百分百，都是零。人弃我不一定取，人抢我一定给。

--摘自《2006-11-16 12:00 教你炒股票7：给赚了指数亏了钱的一些忠告》评论
""",

    "23": """
有人说每天看盘很累很疲惫，关键是对市场没有充分理解，看盘何尝不是一种放松，不能放松，是
因为有烦恼，被烦恼所烦恼，智慧才是最大的放松。
 
--摘自《即缠非缠》微博
""",

    "24": """
在现实中，所谓的天命，都是在人谋之中，只是你的谋划是否完全，另外，一个很重要的是，完全
的谋划是否超越你的能力。

对于股票来说，完全的分类或谋划，基本不存在超越能力的问题，只是买卖多少的问题，有能力就
多点，没能力就少点，不存在某种分类完全不能执行的情况。因此，所有的重点，都在这完全的分
类上了。但完全的分类，不是单层次的，一定也必须是多层次的。本ID的理论最重要的特点之一，
就是自然给出了分类的层次，也就是不同的自然形成的级别。不同的级别，有不同的完全分类，而
综合起来，就有了一个立体的完全分类的系统，这才是我们的操作必须依赖的。

把市场分析好了，把情况分类好了，然后问一下自己，你有这个处理所有可能情况的能力吗？如果
没有，那就算了；如果有，就上。事情就这么简单。

--摘自《2008-02-25 16:32 教你炒股票100：中医、兵法、诗歌、操作3》
""",

    "25": """
小人，虽说是对利益之网而游刃有余，但因为画地为牢，自我小之，为一我所牵，最终不过仍是机
关木人，到头来，被一点聪明所误，一场游戏一场梦而已。而君子，尽知小人所知，行小人之行而
无一我之所牵，不废一法而行千法万法，行千法万法而不立一法，于所知所行而自在。

--摘自《2007-08-20 22:36 《论语》详解：给所有曲解孔子的人（67）》
""",

    "26": """
人，总是自己骗自己；人，只能自己骗自己。没有你自己，谁都骗不到你。

--摘自《2008-01-27 10:15 教你打坐22：佛魔最难除》
""",

    "27": """
你在操作时，你后续的所有可能面对的情况与对策都必须了然，否则你就没资格操作。对于一个真
正的操作者，没有任何情况是意外的，因为，所有的情况都被完全地分类了，所有相应的对策都事
先有了，只是等着市场自己去选择，去触及我们事先给定的开关。

--摘自《2008-02-04 19:51 教你炒股票98：中医、兵法、诗歌、操作2》
""",

    "28": """
市场中，最大的敌人之一，就赌徒心理、赌徒思维。赌，最终的结局就只有一个，如果你以赌徒心
理参与市场，那么你的结局就已经注定，你就算还没再锅里，那也只是养肥了再煮而已，没什么区
别。

赌徒心理一个最大的特点，就是预设一个虚拟的目标，一个想象中的目标，完全无视市场本身。

--摘自《2008-01-23 16:18 教你炒股票96：无处不在的赌徒心理》
""",

    "29": """
市场真正的成功，都是严格的操作下完成的。操作失误了有什么大不了的，市场的机会不断涌现，
一个严格的操作程序，足以保证你长期的成功。

生活，很简单，一天三顿，五谷为养、五果为助、五畜为益、五菜为充，而不是那些古灵精怪的玩
意；市场很简单，就如同生活，在一定的韵律中生长出利润。只有那韵律，那平凡但又能长久的赢
利模式，才能使得你战胜市场。市场，只是生活的一部分，如此而已。

--摘自《2008-01-23 16:18 教你炒股票96：无处不在的赌徒心理》
""",

    "30": """
在本ID这里，只有严格分类后的不同操作类型，没有其他那么多无聊的不切边际的所谓预测。来本
ID这里学习，第一层次，就是要达到：当机立断。

机会，是可以预先分析的，但这分析，不是预测，而是建立在完全分类基础上的边界分划，这分划
完全来自本ID理论的纯数学构造，这构造的唯一性与精确性保证了这分类与边界的当下确认性。任
何一个当下，你都可以根据本ID的理论马上给出后面必然要出现的机会。

--摘自《2008-01-21 17:29 教你炒股票94：当机立断》
""",

    "31": """
学了本ID的理论，脑子里必须时刻有两个字：级别。如果连级别都搞不清楚，你还419？被419还
差不多。有了级别，就是节奏问题了，419，就是见好要收，而不是天长地久，这都不明白，就等
着灾难连连吧。不会卖出，就等于失去了下次买入的机会。这个节奏之所以难，说白了，就是贪嗔
痴疑慢作怪。

--摘自《2008-01-21 17:29 教你炒股票94：当机立断》
""",

    "32": """
投资是一门艺术，而投资的艺术归根结底是资金管理的艺术，这就像歌唱的艺术，归根结底是呼吸
的艺术一样。而市场的波动，归根结底是在前后两个高低点关系构成的一个完全分类中展开的，明
白了这一点，市场就如同自己的掌纹一样举手可见了。

--摘自《2006-05-12 19:02 股市闲谈：G股是G点，大牛不用套！》
""",

    "33": """
艺术高度往往和素材或技术无关，是否能把各种因素结合成一个生命的整体，才是艺术的关键。

--摘自《2006-02-20 10:04 连载1：“睡过”或“消费过”的男人们！》
""",

    "34": """
在市场中，第一就要分清楚预测与操作的严重区别：预测是游戏，是茶余饭后的谈资；而操作是真
刀真枪去干，是血与火的斗争。绝对的预测归根结底都是笑话，而非绝对的操作归根结底是死路一
条。像这次，绝对的操作是怎么样，本ID早已反复说明：3656点站不住走，3300缺口位置不回补
可以回补筹码再短差一把，否则就让大盘越南盾去。这里，整个操作的设计是没有任何不确定的地
方，都是绝对性的，这才能股票股票而不是被股票股票，而任何预测都只能永远在被股票股票的死
路上轮回。

--摘自《2008-06-10 16:40 今年诸多灾难与妖蛾子事的历史性解释》
""",

}

def print_one():
    k = random.choice(list(texts.keys()))
    print(texts[k].strip())
