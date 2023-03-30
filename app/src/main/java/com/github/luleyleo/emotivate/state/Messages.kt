package com.github.luleyleo.emotivate.state

import android.graphics.Bitmap
import androidx.compose.runtime.Immutable

@Immutable
data class Message(
    val author: String,
    val timestamp: String,
    val text: String,
    val image: Bitmap? = null,
    val emotion: Emotion? = null,
)

@Immutable
data class Emotion(val valence: String, val arousal: String) {
    fun emote() = when {
        this.valence == "positive" && this.arousal == "low" -> "\uD83D\uDE0C" // calm
        this.valence == "positive" && this.arousal == "mid" -> "\uD83D\uDE42" // slight smile
        this.valence == "positive" && this.arousal == "high" -> "☺️" // happy
        this.valence == "negative" && this.arousal == "low" -> "\uD83D\uDE22" // sad
        this.valence == "negative" && this.arousal == "mid" -> "\uD83D\uDE41" // slight frown
        this.valence == "negative" && this.arousal == "high" -> "\uD83D\uDE21" // angry
        else -> "\uD83D\uDE15"
    }
}

