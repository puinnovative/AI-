# Results
![](./Imgs/chat.png)<br>
基于seq2seq的生成式的对话机器人（迭代十个周期的结果）

# Model
![](./Imgs/seq2seq.png)

# 漫谈
聊天机器人这块，目前就是LSTM，它相比于simple rnn在处理数据上采用了更加复杂的方式把数据中的各个单一数据联系起来。但是lstm由于数学问题导致一部分信息丢失，因此需要借助概率分布的attention机制来解决时序问题。

具体的数学先不介绍了。

