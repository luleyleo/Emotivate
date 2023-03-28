package com.github.luleyleo.emotivate.state

import android.graphics.Bitmap
import androidx.compose.runtime.Immutable

@Immutable
data class Message(
    val author: String,
    val timestamp: String,
    val text: String,
    val image: Bitmap? = null,
)

