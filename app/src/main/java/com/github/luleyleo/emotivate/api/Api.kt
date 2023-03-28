package com.github.luleyleo.emotivate.api

import okhttp3.MultipartBody
import okhttp3.RequestBody
import okhttp3.ResponseBody
import retrofit2.http.Multipart
import retrofit2.http.POST
import retrofit2.http.Part

interface NeuralService {
    @Multipart
    @POST("api/audio")
    suspend fun getAffectArousalDiagram(@Part("transcript") transcript: RequestBody, @Part audio: MultipartBody.Part): ResponseBody
}