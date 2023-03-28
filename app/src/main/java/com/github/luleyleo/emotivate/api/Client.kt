package com.github.luleyleo.emotivate.api

import android.graphics.Bitmap
import android.graphics.BitmapFactory
import okhttp3.MediaType
import okhttp3.RequestBody
import retrofit2.Retrofit
import java.io.File

class Client {
    private val retrofit: Retrofit
    private val neuralService: NeuralService

    private val mediaString = MediaType.parse("text/plain")
    private val mediaAudio = MediaType.parse("audio/mpeg")

    init {
        retrofit = Retrofit.Builder()
            .baseUrl("https://8313-137-250-27-12.eu.ngrok.io")
            .build()

        neuralService = retrofit.create(NeuralService::class.java)
    }

    suspend fun getAffectArousalDiagram(message: String, audio: File): Bitmap {
        val transcriptBody = RequestBody.create(mediaString, message)
        val audioBody = RequestBody.create(mediaAudio, audio)

        val response = neuralService.getAffectArousalDiagram(transcriptBody, audioBody)

        val imageBytes = response.bytes()
        val bitmap = BitmapFactory.decodeByteArray(imageBytes, 0, imageBytes.size)

        return bitmap
    }
}
