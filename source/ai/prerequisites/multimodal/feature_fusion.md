# 特征融合

多模态特征融合的方法大体分为三种：前端融合、中间融合和后端融合。

## 前端融合

将多个独立的数据集融合成一个单一的特征向量，然后输入到机器学习分类器中。

多模态前端融合方法常常与特征提取方法相结合以剔除冗余信息，如主成分分析（PCA）、最大相关最小冗余算法（mRMR）、自动解码器（Autoencoders）等。

本人研究的是使用深层联合自编码模型，将三种模态的特征使用三层线性层将维度转化为同一维度，然后相加，最后将三者进行还原回去。

## 中间融合

指的是将不同的模态数据先转化为高维特征表达，再于模型的中间层进行融合。以神经网络为例，中间融合首先利用神经网络将原始数据转化成高维特征表达，然后获取不同模态数据在高维空间上的共性。在问答对话中有 [MFB 方法](https://github.com/yuzcccc/vqa-mfb)，它针对文本和图像两种模态，先将每个模态特征转化为相同维度的高维向量，然后进行逐元素相乘，最后进行 sum pooling 操作。

## 后端融合

指的是将不同模态数据分别训练好的分类器输出打分(决策)进行融合。常见的后端融合方式包括最大值融合(max-fusion)、平均值融合(averaged-fusion)、 贝叶斯规则融合(Bayes’rule based)以及集成学习(ensemble learning)等。

下面介绍比较实用的专门总结多模态融合文章的网址（里面都是关于多模态的高水平论文）：

里面会注明是否含有开源代码，文章出处，很齐全：网址：https://github.com/pliang279/awesome-multimodal-ml#multimodal-fusion

综述文章：

深度多模态表征学习：一项调查，该文章通过对深度学习中多模态数据方法进行总结和讨论，分析方法种类和各自优缺点。网址：https://ieeexplore.ieee.org/abstract/document/8715409