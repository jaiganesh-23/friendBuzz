<script setup>
import 'vue3-carousel/carousel.css'
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'

const carouselConfig = {
  itemsToShow: 3,
  wrapAround: true,
  autoplay: 3000,
  pauseAutoplayOnHover: true,
}
const apiUrl = import.meta.env.VITE_API_URL
</script>

<template>
  <main>
    <p class="welcome-text text-5xl text-center">Welcome to FriendBuzz!</p>

    <div class="mt-10 welcome-div flex justify-evenly">
      <div class="p-8 w-[40vw] text-2xl">
        <p class="">Login to explore other people's posts, make friends, chat and view your profile. Dont Miss any updates with notifications and stay up to date with trends.
        </p>
        <div class="mt-4">
          <RouterLink to="/login" class="p-3 bg-[#410445] text-white rounded-lg">Login</RouterLink>
        </div>
      </div>
      <div class="p-4 w-[40vw] text-2xl">
        <p class="">Dont have an account?, click below to signup and start exploring the world of FriendBuzz.
        </p>
        <div class="mt-4">
          <RouterLink to="/signup" class="p-3 bg-[#410445] text-white rounded-lg">Signup</RouterLink>
        </div>
      </div>
    </div>

    <div class="mt-10">
      <p class="text-4xl text-center">Features of FriendBuzz</p>
      <div class="w-[80vw] mx-auto mt-5">
      <Carousel v-bind="carouselConfig">
        <Slide>
          <div class="carousel__item p-5 w-[80%] rounded-lg">
            <img :src="`${apiUrl}/media/view_and_add_posts.png`"  alt="" class="w-full h-60 rounded-lg">
            <p class="text-md text-center text-[#F6DC43]">View and Add Posts</p>
            <p class="text-sm">You can explore other's posts in the feed and upload your posts</p>
          </div>
        </Slide>

        <Slide>
          <div class="carousel__item p-5 w-[80%] rounded-lg">
            <img :src="`${apiUrl}/media/chat_with_others.png`"  alt="" class="w-full h-60 rounded-lg">
            <p class="text-md text-center text-[#F6DC43]">Chatting</p>
            <p class="text-sm">You can chat with your friends and others with a message request</p>
          </div>
        </Slide>

        <Slide>
          <div class="carousel__item p-5 w-[80%] rounded-lg">
            <img :src="`${apiUrl}/media/notifications.png`"  alt="" class="w-full h-60 rounded-lg">
            <p class="text-md text-center text-[#F6DC43]">Notfications</p>
            <p class="text-sm">Stay up to date with notifications when something happens</p>
          </div>
        </Slide>

        <Slide>
          <div class="carousel__item p-5 w-[80%] rounded-lg">
            <img :src="`${apiUrl}/media/people_you_may_know_and_trends.png`"  alt="" class="w-full h-60 rounded-lg">
            <p class="text-md text-center text-[#F6DC43]">Trends and People You May Know</p>
            <p class="text-sm">Stay updated with current trends and find people you may know</p>
          </div>
        </Slide>

        <Slide>
          <div class="carousel__item p-5 w-[80%] rounded-lg">
            <img :src="`${apiUrl}/media/search.png`"  alt="" class="w-full h-60 rounded-lg">
            <p class="text-md text-center text-[#F6DC43]">Search</p>
            <p class="text-sm">Search for people and posts</p>
          </div>
        </Slide>

        <Slide>
          <div class="carousel__item p-5 w-[80%] rounded-lg">
            <img :src="`${apiUrl}/media/like_and_comment_posts.png`"  alt="" class="w-full h-60 rounded-lg">
            <p class="text-md text-center text-[#F6DC43]">Engage with posts</p>
            <p class="text-sm">Like and comment posts</p>
          </div>
        </Slide>

        <template #addons>
          <Navigation />
          <Pagination />
        </template>
      </Carousel>
    </div>
    </div>

  </main>
</template>

<style>
.carousel {
  --vc-nav-background: rgba(0, 0, 0, 0.3);
  --vc-nav-color: white;
  --vc-nav-color-hover: #e5e5e5;
  --vc-nav-border-radius: 50%;
  --vc-nav-width: 40px;
  --vc-nav-height: 40px;
}
.carousel {
  --vc-pgn-background-color: white;
  --vc-pgn-active-color: #F6DC43;
  --vc-pgn-height: 8px;
  --vc-pgn-width: 8px;
}
.welcome-div > div{
  background-color: rgb(0, 0, 0, 0.9);
  color: white;
  border-radius: 20px;
}

.carousel__item{
  background-color: rgb(0, 0, 0, 0.9);
  color: white;
}
</style>

