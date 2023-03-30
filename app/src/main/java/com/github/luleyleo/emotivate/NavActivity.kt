package com.github.luleyleo.emotivate

import android.os.Bundle
import androidx.activity.compose.setContent
import androidx.activity.viewModels
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.WindowCompat
import com.github.luleyleo.emotivate.conversation.ConversationContent
import com.github.luleyleo.emotivate.state.ConversationViewModel
import com.github.luleyleo.emotivate.theme.JetchatTheme

/**
 * Main activity for the app.
 */
class NavActivity : AppCompatActivity() {
    private val viewModel: ConversationViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Turn off the decor fitting system windows, which allows us to handle insets,
        // including IME animations
       //WindowCompat.setDecorFitsSystemWindows(window, false)

        setContent {
            JetchatTheme {
                ConversationContent(
                    model = viewModel,
                    navigateToProfile = {},
                    onNavIconPressed = {}
                )
            }
        }
    }
}
