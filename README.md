 As data-driven decision-making and recommenders systems are gaining ground the
 quality, and fairness rankings have become major issues that should be carefully studied.
 These problems are highly linked to how individuals in a ranking are ordered. In
 a real-world context, items in a list can either be ordered according to their relevance
 or group affiliation. Relevance indicates how useful an individual is to the user. On the
 other hand, group affiliation indicates to what social, ethnic, or gender group someone
 belongs. Ranking algorithms are used in various applications, such as search engines,
 recommendation systems, and information retrieval systems. These algorithms rely on
 relevance scores to create rankings, which help users find the most relevant information
 or products. relevance scores are also critical in evaluating the quality and fairness of
 a ranking. However, the influence of the underlying distribution of relevance scores
 on the corresponding metrics has not been extensively studied yet. Therefore, further
 research is needed to investigate the impact of relevance score distributions on ranking
 metrics. In addition, analyzing the statistical distribution of relevance scores can lead
 to improvements in ranking algorithms by allowing us to choose the appropriate metrics
 to evaluate rankings based on the relevance score distribution. Our study can serve as
 a starting point for a realistic evaluation of rankings since there is currently no previous
 research on how varying relevance scores impact ranking quality. To achieve that,
 we will compare different quality and fairness metrics under varying relevance score
 distributions. This comparison will allow us to extract insights on when each metric is
 most appropriate and which ones are more likely to capture biases present in real-life
 rankings. For example, we can model whether individuals belonging to certain groups
 are perceived as more or less relevant and how this impacts the quality and fairness of a
 ranking. To achieve that our overall experimental setting can be divided into two parts.
 Initially, our attention will be directed toward assessing the quality metrics– specifically,
 DCG, MRR, and NDCG. For every metric, we will derive relevance scores from diverse
 distributions (Normal, Uniform, Beta, Gamma, and Bimodal). Subsequently, we will
 arrange items in ascending, descending, or random according to their relevance within
 the ranking. The ensuing step involves observing how the quality metrics change in
 response to alterations in the distributions’ means and standard deviations.
 Following this, we will shift our attention to the assessment of fairness metrics, specifically
 DTD, DTR, DID, and DIR. In evaluating fairness metrics, we will generate rankings
 where each individual is assigned a group affiliation (protected or non-protected) and
 relevance scores. Similar to the evaluation of quality metrics, relevance scores will be
 drawn from various distributions, with adjustments to means and standard deviations.
 Additionally, within each group, items will be organized in ascending, descending, or
 random order based on their relevance. This phase of the study will encompass different
 scenarios of dominance between the protected and non-protected groups. Specifically, we
 will simulate situations where protected individuals are predominantly positioned at the
 ranking’s top, receiving higher relevance scores compared to non-protected individuals.
 The primary aim of this study is to comprehensively explain the role that relevance
 scores play in the quality and fairness of rankings. By examining how these metrics
 respond to various scenarios of relevance score distribution, ranking, or dominance, we
 seek to uncover insights that can guide the design and optimization of more effective
 and equitable recommendation algorithms.
 To achieve this overarching goal, we formulate the following research questions:
 How do different relevance score distributions, including Normal, Uniform, Beta, Gamma,
 and Bimodal, impact the quality and fairness metrics?
 What are the effects of altering means and standard deviations in relevance score
 distributions on the observed changes in quality and fairness metrics?
 To what extent do fairness metrics exhibit variation in dominance scenarios, and which
 of these metrics prove adept at effectively differentiating between such scenarios?
