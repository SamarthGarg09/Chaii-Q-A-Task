from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import gradio as gr

title = 'Ask a Question in popular languages like English, German, French, Hindi, Tamil, etc'
description = '''It is a question answering model that can answer questions. The model is fine-tuned on chaii dataset by Google.
To know more visit my <a href="https://huggingface.co/SmartPy/bert-finetuned-squad-chaii">model page</a> and also feel free to check the 
<a href="https://github.com/SamarthGarg09/Chaii-Q-A-Task">github repo</a> .
'''
article="""
    User has to type/paste a question along with the context in the text boxes provided. In return he/she will get the answer to the question along with the score. 
"""
examples=[["सन १८८६ में किसने बताया कि तम्बाकू में मोजेक रोग एक विशेष प्रकार के वाइरस के द्वारा होता है?",
"""विषाणु अकोशिकीय अतिसूक्ष्म जीव हैं जो केवल जीवित कोशिका में ही वंश वृद्धि कर सकते हैं।[1] ये नाभिकीय अम्ल और प्रोटीन से मिलकर गठित होते हैं, शरीर के बाहर तो ये मृत-समान होते हैं परंतु शरीर के अंदर जीवित हो जाते हैं। इन्हे क्रिस्टल के रूप में इकट्ठा किया जा सकता है। एक विषाणु बिना किसी सजीव माध्यम के पुनरुत्पादन नहीं कर सकता है। यह सैकड़ों वर्षों तक सुशुप्तावस्था में रह सकता है और जब भी एक जीवित मध्यम या धारक के संपर्क में आता है उस जीव की कोशिका को भेद कर आच्छादित कर देता है और जीव बीमार हो जाता है। एक बार जब विषाणु जीवित कोशिका में प्रवेश कर जाता है, वह कोशिका के मूल आरएनए एवं डीएनए की जेनेटिक संरचना को अपनी जेनेटिक सूचना से बदल देता है और संक्रमित कोशिका अपने जैसे संक्रमित कोशिकाओं का पुनरुत्पादन शुरू कर देती है।\nविषाणु का अंग्रेजी शब्द वाइरस का शाब्दिक अर्थ विष होता है। सर्वप्रथम सन १७९६ में डाक्टर एडवर्ड जेनर ने पता लगाया कि चेचक, विषाणु के कारण होता है। उन्होंने चेचक के टीके का आविष्कार भी किया। इसके बाद सन १८८६ में एडोल्फ मेयर ने बताया कि तम्बाकू में मोजेक रोग एक विशेष प्रकार के वाइरस के द्वारा होता है। रूसी वनस्पति शास्त्री इवानोवस्की ने भी १८९२ में तम्बाकू में होने वाले मोजेक रोग का अध्ययन करते समय विषाणु के अस्तित्व का पता लगाया। बेजेर्निक और बोर ने भी तम्बाकू के पत्ते पर इसका प्रभाव देखा और उसका नाम टोबेको मोजेक रखा। मोजेक शब्द रखने का कारण इनका मोजेक के समान तम्बाकू के पत्ते पर चिन्ह पाया जाना था। इस चिन्ह को देखकर इस विशेष विषाणु का नाम उन्होंने टोबेको मोजेक वाइरस रखा।[2]\nविषाणु लाभप्रद एवं हानिकारक दोनों प्रकार के होते हैं। जीवाणुभोजी विषाणु एक लाभप्रद विषाणु है, यह हैजा, पेचिश, टायफायड आदि रोग उत्पन्न करने वाले जीवाणुओं को नष्ट कर मानव की रोगों से रक्षा करता है। कुछ विषाणु पौधे या जन्तुओं में रोग उत्पन्न करते हैं एवं हानिप्रद होते हैं। एचआईवी, इन्फ्लूएन्जा वाइरस, पोलियो वाइरस रोग उत्पन्न करने वाले प्रमुख विषाणु हैं। सम्पर्क द्वारा, वायु द्वारा, भोजन एवं जल द्वारा तथा कीटों द्वारा विषाणुओं का संचरण होता है परन्तु विशिष्ट प्रकार के विषाणु विशिष्ट विधियों द्वारा संचरण करते हैं।\n"वायरस कोशिका के बाहर तो मरे हुए ऱहते है लेकिन जब ये कोशिका मैंं प्रवेश करते है तो इनका जीवन चक्र प्रारम्भ होने लगता है "by siddharth lodha ratlai.\n सन्दर्भ \n\nश्रेणी:विषाणु\nश्रेणी:सूक्ष्मजैविकी\nश्रेणी:हिन्दी विकि डीवीडी परियोजना
"""
]]

tokenizer = AutoTokenizer.from_pretrained("SmartPy/bert-finetuned-squad-chaii")
model = AutoModelForQuestionAnswering.from_pretrained("SmartPy/bert-finetuned-squad-chaii")

nlp = pipeline("question-answering", model=model, tokenizer=tokenizer)

def qa(question, context):
    return nlp(question=question, context=context)["answer"], nlp(question=question, context=context)["score"]
textbox1 = gr.Textbox(label="Type your question:", placeholder="John Doe", lines=2)
textbox2 = gr.Textbox(label="Type your context:", placeholder="John Doe", lines=2)

textbox3 = gr.Textbox(label="Answer:", placeholder="John Doe", lines=2)
textbox4 = gr.Textbox(label="Score:", placeholder="0.9", lines=2)

gr.Interface(qa, inputs=[textbox1, textbox2], outputs=[textbox3, textbox4], title=title, article=article, description=description, examples=examples).launch()