package com.github.luleyleo.emotivate.state

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.github.luleyleo.emotivate.api.Client
import kotlinx.coroutines.launch
import java.io.File

class ConversationViewModel(initialState: ConversationUiState = ConversationUiState()) : ViewModel() {
    var uiState = initialState
        private set

    private var client = Client()

    fun sendMessage(transcript: String, audio: File) {
        uiState.addMessage(Message("me", "now", transcript))

        viewModelScope.launch {
            try {
                val diagram = client.getAffectArousalDiagram(transcript, audio)
                uiState.addMessage(Message("bot", "now", "Your emotions:", diagram))
            } catch (e: Exception) {
                uiState.addMessage(Message("bot", "now", "Error:\n" + e.message))
            }
        }
    }
}