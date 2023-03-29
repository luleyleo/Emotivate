package com.github.luleyleo.emotivate.api

import android.graphics.Bitmap
import android.graphics.BitmapFactory
import okhttp3.FormBody
import okhttp3.MediaType
import okhttp3.MultipartBody
import okhttp3.RequestBody
import retrofit2.Retrofit
import java.io.File

class Client {
    private val retrofit: Retrofit
    private val neuralService: NeuralService

    private val mediaString = MediaType.parse("text/plain")
    private val mediaAudio = MediaType.parse("audio/wav")

    init {
        retrofit = Retrofit.Builder()
            .baseUrl("https://eba8-137-250-27-8.eu.ngrok.io")
            .build()

        neuralService = retrofit.create(NeuralService::class.java)
    }

    suspend fun getAffectArousalDiagram(message: String, audio: File): Bitmap {
        val response = neuralService.getAffectArousalDiagram(
            RequestBody.create(mediaString, message),
            MultipartBody.Part.createFormData("audio", "audio.wav", RequestBody.create(mediaAudio, audio))
        )

        val imageBytes = response.bytes()
        val bitmap = BitmapFactory.decodeByteArray(imageBytes, 0, imageBytes.size)

        return bitmap
    }
}
