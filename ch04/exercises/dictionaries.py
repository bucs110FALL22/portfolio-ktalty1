article ="""
Dogs are more than just cuddly companions — research continues to show that pets bring real health benefits to their owners. Having a dog around can lead to lower levels of stress for both adults and kids. They’ve been found to decrease the risk of asthma in children and have been linked to lower blood pressure. And researchers have also shown that dog owners are more active than those who don’t own dogs, packing in more steps per day on their walks or just regular playtime. Last month, a study showed that older dog owners take 2,760 more steps per day on average compared to non-owners, which amounted to an additional 23 daily minutes of moderate exercise. Now, a new study in the Journal of Epidemiology and Community Health shows how enduring that phenomenon is: dog owners are also significantly more active during the winter. 
Have a pet of your own? The researchers found that the the people who didn’t own a dog were sedentary for about 30 more minutes a day on average than those who walked their dogs. Everyone who participated in the study was less active on shorter days, colder days and days with more precipitation. But the researchers discovered that, even during days with bad weather, dog walkers were more active than non-dog walkers were on the nicest days. “We were amazed to find that dog walkers were on average more physically active and spent less time sitting on the coldest, wettest, and darkest days than non-dog owners were on long, sunny, and warm summer days,” project lead Andy Jones, a UEA professor, said in a press release. Dog walkers got in an average 12 more minutes of activity on the wettest days, for example, than those who don’t own dogs got on the driest days. Overall on the driest days, dog walkers were sedentary for an average of 632 minutes, compared to non-dog owners’ 661 minutes. Jones said this finding could have important implications about how to motivate people to stay active as they age.
"""



substiutions = {
"dog":"dragons",
"animals":"friends",
"walkers":"people",
"cuddly":"scary",
"active":"hungry",
"stress":"motivation"  
}

for key, value in substiutions.items():
  article  = article.replace(key, value)

print(article)
