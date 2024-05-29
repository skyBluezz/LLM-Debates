

# Part 2: Kanji Stable Diffusion 


This one was quite fun and brought me back to the days of learning Chinese :)!  A large portion of this problem was data engineering, where the associated code resides in [dataExtraction/main.py](dataExtraction/main.py).  For the sake of time and simplicity, I did not attempt to train a SD model from scratch.  From my days in graduate school I recall this can be arduous, particularly if you have to do greedy-wise training of the successive layers in the VAE.  To expedite this I fine tuned on two HuggingFace models: [CompVis 1.4](https://huggingface.co/CompVis/stable-diffusion-v1-4) and [SD-Nano-2.1](https://huggingface.co/bguisard/stable-diffusion-nano-2-1) (built particularly for 128x128 images).  This pipeline should be relatively ready to run on your own.  Call ./launch_training.sh in top-level directory to begin training (may require HF account and key).

I will link results of the CompVis 1.4 below, after 20k train iterations and playing with batch sizes, learning rate, and wrangling with data formats to match HF requirements.  I found a few of these to be funny and interesting.  

Buzz Aldrin             |  Ferrari
:----------------------:|:---------------------------:
![](<./example_outputs/Buzz aldrin.png>)  |  ![](example_outputs/Ferrari.png)
*‘hoshi’ like character representing ‘star’ and 'yue'-like character for moon* | *‘kane’ or ‘kin’ like character representing ‘money’*

 Moon             |  Instagram
:----------------------:|:---------------------------:
![](<./example_outputs/Full Moon.png>)  |  ![](example_outputs/Instagram.png)
*‘Yue’ like character for ‘moon’* | *I oddly thought this looked like app icon for Instagram! Lol*


 Bible | All Examples
:----------------------:|:----------------------:
![](<./example_outputs/Bible.png>)  | ![](<./collated_examples.png>)
*The character on the left represents a person.  Can be associated with belief, idea, truth, service.* | All examples 

I brought these results to a couple friends who are Japense-born.  Some feedback I got -- the balance (left/right) is relatively good.  Most of these still do not make sense though (-_-).  A lot of this Kanji is also over-complex, with more strokes than usual, and some of this may be due to the fact that I often queried for two-word phrases, like 'Sphagetti Western' or 'Shohei Ohtani' or 'Gauss Law'.  These would require more than one character, and perhaps the model is trying to over-squeeze strokes to compensate.  For example "small dog with huge head" leads to a totally complicated output..

Overall this was a fun problem and it was neat to learn more about the nature of kanji
