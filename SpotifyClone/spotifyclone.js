console.log("hello ")
let currFolder;
let currentAudio=new Audio()

// wrong approach
//a fn which returns a promise and gets resolved when an album is clicked
// function givefolder(){
//     return new Promise((resolve,reject)=>{
    //     let folderarray=Array.from(document.querySelector(".albumCards").children);
    //     // console.log(folderarray);
    //     folderarray.forEach((f)=>{
    //         f.addEventListener("click",() => {
    //             currFolder=f.querySelector(".albumname").innerHTML;
    //             console.log("inside promise",currFolder);
    //             document.querySelector(".audiofiles").innerHTML="";
    //             resolve(currFolder);
    //             main();
    //         }
    //     )
    // })
//     })

// }

// This function loads all the audio files from the directory and puts the links into an array and returns it

async function getaudioFiles(folder){
    console.log("req folder",folder)
    let a=await fetch(`https://s3.ap-south-1.amazonaws.com/spoifyclone.audiofiles/songlist/index.html`);
    let ahtml = await a.text();
    // console.log(ahtml);
    
    let div=document.createElement("div")
    div.innerHTML=ahtml;
    let audioNames=div.getElementsByTagName("a")
    // console.log(audioNames);
    
    let audioFiles=[];
    for (let i = 1; i < audioNames.length; i++) {
        const element = audioNames[i];
        // console.log("ele",element)
        if(element.href.endsWith(".mp3") || element.href.endsWith(".wav")){
            audioFiles.push(element.href)
        }
    }
    console.log("asu",audioFiles)
    for (let i = 0; i < audioFiles.length; i++) {
        const element = audioFiles[i];
        finalname=element.replaceAll("%20"," ")
        // console.log("forloop",currFolder)
        finalname=finalname.split(`/${currFolder}`)[1];
        // or decodeuri can be used
        // finalname=decodeURI(element).split('/songlist/')[1]
        // console.log(list);

        let list=document.createElement("li");
        // list.setAttribute("class","scaleffectForplaylist liaudio");
        document.querySelector(".audiofiles").append(list);
        list.innerHTML=`<img src="music.svg" class="musicicon invert">
                        <div class="details">
                            <div>${finalname}</div>
                            <div>Akshay R</div>
                        </div>
                        <div class="playnow">
                            <div class="inline">Play Now</div>
                            <img src="playbarPlay.svg" class="invert playlistPlayicon">
                        </div>`;

        console.log("mememe",document.querySelector(".audiofiles"))
        // document.querySelector(".audiofiles").append("list");

        console.log("i am listu",list);
        
    }

    //array of all the list elements 
    liarray=Array.from(document.querySelector(".audiofiles").getElementsByTagName("li"));
    console.log("li",liarray);
    
    // adding event listners to the playlist cards,prev,next
    liarray.forEach((ele,index) => {
        ele.addEventListener("click",() => {
            // currentAudio=new Audio(files[index]) ---> everytime a new audio tag gets created and thus the previous keeps plying while the currentaudio is played
            // console.log(playaudio(index));
            playaudio(index);
            // console.log(currentAudio.duration)
            
            document.getElementById("previous").addEventListener("click",() => {
                playaudio(index-1);
                index--;
            })
            document.getElementById("next").addEventListener("click",() => {
                playaudio(index+1);
                index++;
            })
        }) 
    })

    return audioFiles;
}

async function getalbumNames(){
    let a=await fetch("https://s3.ap-south-1.amazonaws.com/spoifyclone.audiofiles/songlist/index.html");
    let ahtml = await a.text();
    
    let div=document.createElement("div")
    div.innerHTML=ahtml;
    let albumCollection=div.getElementsByTagName("a")
    let albumNames=Array.from(albumCollection)

    let albumFiles=[];
    for (let i = 1; i < albumNames.length; i++) {
        const element = albumNames[i];
        console.log(element);
        if(element.href.endsWith("/")){
            finalname=element.href.split("/songlist/")[1];
            albumFiles.push(finalname);
            let divalbum=document.createElement("div");
            divalbum.setAttribute("class","card");
            document.querySelector(".albumCards").append(divalbum);

            divalbum.innerHTML=`<div class="albumPic">
                                <button class="play tran">
                                    <img src="playbutton.svg" class="playicon">
                                </button>
                            </div>
                            <div class="albumname">${finalname}</div>
                            <div class="albumdetails">asdd</div>`;
        }
    }
    console.log(albumFiles)

    let folderarray=Array.from(document.querySelector(".albumCards").children);
        // console.log(folderarray);
        folderarray.forEach((f)=>{
            f.addEventListener("click",async() => {
                currFolder=f.querySelector(".albumname").innerHTML;
                console.log("inside promise",currFolder);
                document.querySelector(".audiofiles").innerHTML="";
                files=await getaudioFiles(currFolder);
                console.log("filesunderfolder",files);
            }
        )
    })

    return albumFiles;
}

//function to play the audio whenever called
const playaudio =(i)=>{
    document.getElementById("play").src="pause.svg";    
    currentAudio.src = files[i];
    currentAudio.play();
    // console.log(liarray[i].querySelector(".details").children[0].innerHTML)
    document.querySelector(".songinfo").innerHTML=liarray[i].querySelector(".details").children[0].innerHTML
    document.querySelector(".songtime").innerHTML="00:00 / 00:00"
}

function secondsToMinutesSeconds(seconds) {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = Math.round(seconds % 60); // Round to two digits

    const formattedMinutes = String(minutes).padStart(2, '0');
    const formattedSeconds = String(remainingSeconds).padStart(2, '0');

    return `${formattedMinutes}:${formattedSeconds}`; 
}

// (async function(){
    // albumFiles=await getalbumNames()
    // console.log("albumFiles",albumFiles)

    // currFolder=await givefolder();
    // console.log("currfolder",currFolder);
// })();

// This async function calls the getaudioFiles fn and awaits for it, after it gets it inserts them into the ul and further
async function main(){
    //adding the albumbs to the web based on the folders saved
    

    //adding event listeners for the cards and waiting for response
    // currFolder=await givefolder();
    // console.log("currfolder",currFolder);
    albumFiles=await getalbumNames()

    // Attach an event listener to play, next and previous
    play.addEventListener("click", () => {
        if (currentSong.paused) {
            currentSong.play()
            play.src = "img/pause.svg"
        }
        else {
            currentSong.pause()
            play.src = "img/play.svg"
        }
    })
    // adding event listening to play/pause button
    document.getElementById("play").addEventListener("click",() => {
        console.log(currentAudio)
        if(currentAudio.paused){
            console.log("play",currentAudio)
            currentAudio.play();
            document.getElementById("play").src="pause.svg";
        }

        else{
            console.log("pause",currentAudio)
            currentAudio.pause();
            document.getElementById("play").src="playbarPlay.svg";
        }
    })

    // to listen current time of the audio :
    currentAudio.addEventListener("timeupdate",()=>{
        // console.log(currentAudio.currentTime,currentAudio.duration)
        document.querySelector(".songtime").innerHTML=`${secondsToMinutesSeconds(currentAudio.currentTime)} / ${secondsToMinutesSeconds(currentAudio.duration)}`;

        document.querySelector(".circle").style.left=(currentAudio.currentTime/currentAudio.duration) *100 +"%";

        document.querySelector(".timefill").style.width = (currentAudio.currentTime/currentAudio.duration) *100 +"%";
    })

    document.querySelector(".seekbar").addEventListener("click",(ele)=>{
        //to get all info abt offsets and exact widths of any element : target.getBoundingClientRect())
        // console.log(ele.offsetX,ele.target.getBoundingClientRect())
        // console.log(ele.target.getBoundingClientRect().width/ele.offsetX)*100;

        let percentagecompleted=ele.offsetX/ele.target.getBoundingClientRect().width*100;
        document.querySelector(".circle").style.left=percentagecompleted +"%";
        // document.querySelector(".songtime").innerHTML
        currentAudio.currentTime=(currentAudio.duration*percentagecompleted)/100;
        document.querySelector(".timefill").style.width =percentagecompleted +"%";
    })

    // adding responsiveness
    document.querySelector(".hambdiv").addEventListener("click",()=>{
        // console.log("i got clicked")
        // console.log(document.querySelector(".navbar"))
        document.querySelector(".navbar").style.left="0%";
        // document.querySelector(".navbar").style.left="0%";
    })
    document.querySelector(".closeham").addEventListener("click",()=>{
        // console.log("i got clicked")
        // console.log(document.querySelector(".navbar"))
        document.querySelector(".navbar").style.left="-130%";
        // document.querySelector(".navbar").style.left="0%";
    })

    document.querySelector(".range").addEventListener("change",(e) => {
        // console.log(e.target.value,e,typeof(e.target.value));
        rangevalue=e.target.value;
        currentAudio.volume=parseInt(rangevalue)/100;
    })
}

// way - 2 : without promise : calling main() using givefolder fn
// function givefolder(){
//     folderarray=Array.from(document.querySelector(".albumCards").children);
//     folderarray.forEach((f)=>{
//         f.addEventListener("click",() => {
//             currFolder=f.querySelector(".albumname").innerHTML;
//             console.log(currFolder);
//             document.querySelector(".audiofiles").innerHTML="";
//             main(currFolder)
//         }
//     )
// })
// }

// givefolder()

main()






