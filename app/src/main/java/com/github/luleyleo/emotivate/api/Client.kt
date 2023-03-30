package com.github.luleyleo.emotivate.api

import android.graphics.Bitmap
import android.graphics.BitmapFactory
import com.github.luleyleo.emotivate.state.Emotion
import okhttp3.MediaType
import okhttp3.MultipartBody
import okhttp3.OkHttpClient
import okhttp3.RequestBody
import retrofit2.Retrofit
import java.io.File
import java.util.concurrent.TimeUnit


class Client {
    private val retrofit: Retrofit
    private val neuralService: NeuralService

    private val mediaString = MediaType.parse("text/plain")
    private val mediaAudio = MediaType.parse("audio/wav")

    init {
        val httpClient = OkHttpClient.Builder()
            .connectTimeout(5, TimeUnit.SECONDS)
            .readTimeout(60, TimeUnit.SECONDS)
            .build()

        retrofit = Retrofit.Builder()
            .client(httpClient)
            .baseUrl("https://3e69-137-250-27-7.eu.ngrok.io")
            .build()

        neuralService = retrofit.create(NeuralService::class.java)
    }

    suspend fun getTranscript(audio: File): String {
        val response = neuralService.getTranscript(
            MultipartBody.Part.createFormData("audio", "audio.wav", RequestBody.create(mediaAudio, audio))
        )

        return response.string()
    }
    suspend fun getAffectArousalDiagram(message: String, audio: File): Bitmap {
        val response = neuralService.getAffectArousal(
            RequestBody.create(mediaString, message),
            MultipartBody.Part.createFormData("audio", "audio.wav", RequestBody.create(mediaAudio, audio))
        )

        val imageBytes = response.bytes()
        val bitmap = BitmapFactory.decodeByteArray(imageBytes, 0, imageBytes.size)

        return bitmap
    }

    suspend fun getAffectArousal(message: String, audio: File): Emotion {
        val response = neuralService.getAffectArousal(
            RequestBody.create(mediaString, message),
            MultipartBody.Part.createFormData("audio", "audio.wav", RequestBody.create(mediaAudio, audio))
        )
        val emotions=response.string().split(",")
        return Emotion(emotions[0], emotions[1])
    }
}
