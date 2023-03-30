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
        this.valence == "positive" && this.arousal == "low" -> "\uD83D\uDE04"
        this.valence == "positive" && this.arousal == "mid" -> "\uD83D\uDE04"
        this.valence == "positive" && this.arousal == "high" -> "\uD83D\uDE04"
        this.valence == "negative" && this.arousal == "low" -> "\uD83D\uDE04"
        this.valence == "negative" && this.arousal == "mid" -> "\uD83D\uDE04"
        this.valence == "negative" && this.arousal == "high" -> "\uD83D\uDE04"
        else -> "\uD83D\uDE15"
    }
}

