package com.github.luleyleo.emotivate.state

import androidx.compose.runtime.toMutableStateList

class ConversationUiState(
    initialMessages: List<Message> = listOf()
) {
    private val _messages: MutableList<Message> = initialMessages.toMutableStateList()
    val messages: List<Message> = _messages

    fun addMessage(msg: Message) {
        _messages.add(0, msg)
    }
}
