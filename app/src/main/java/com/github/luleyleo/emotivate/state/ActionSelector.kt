package com.github.luleyleo.emotivate.state

import android.util.Log

class ActionSelector {
    val pl: String="There's nothing to do but staying this calm, watch a movie"
    val pm: String="Please stay this positive, what about a learning session in anki?"
    val ph: String="Stay this happy while checking out a podcast on spotify"

    val nl: String="You seem to be sad, on https://www.roundhousekick.de/ you'll find content to cheer you up, like the following:\n\n Chuck Norris tells Simon what to say"
    val nm: String="Don't be that negative, maybe going to the gym will cheer you up"
    val nh: String="You don't need to be this angry, maybe you should play a few rounds flappy bird to calm down"

    constructor ()  {

    }

    // high med low ==arousal
    // positive negative==valence
    fun selectAction(valence: String, arousal:String): String {

        if (valence=="positive" && arousal=="low"){
            return pl
        }
        else if (valence=="positive" && arousal=="mid"){
            return pm
        }
        else if (valence=="positive" && arousal=="high"){
            return ph
        }

        else if (valence=="negative" && arousal=="low"){
            return nl
        }
        else if (valence=="negative" && arousal=="mid"){
            return nm
        }
        else if (valence=="negative" && arousal=="high"){
            return nh
        }
        Log.d("ConversationScreen", "v:" + valence + "a:" + arousal )

        return "Something went wrong (Errorcode: 42)"
    }





}

