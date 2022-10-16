// const{ Storage } = require("@google-cloud/storage");
// const express = require("express");
// const cors = require("cors");
// const { format } = require("util");
// const Multer = require("multer");
// const cookieParser = require("cookie-parser")

// const app = express();
// const port = 5000;
// const multer = Multer({
//   storage: Multer.memoryStorage(),
//   limits: {
//     fileSize: 5 * 1024 * 1024, // no larger than 5mb, you can change as needed.
//   },
// });
// app.use(cors());
// app.use(cookieParser())


// const cloudStorage = new Storage({
//   keyFilename: `${__dirname}/cred_key.json`,
//   projectId: "cloud-api-test-365605",
// });

// app.post("/api/interview/uploadFile", multer.single("file"), function (req, res, next) {

//     // const body = JSON.parse(req.body)

//     const bucketName = `data/${req.cookies['interview_id']}/${req.cookies['question_number']}`;
//     const bucket = cloudStorage.bucket(bucketName);

//   if (!req.file) {
//     res.status(400).send("No file uploaded.");
//     return;
//   }
//   const blob = bucket.file(req.file.originalname);
//   const blobStream = blob.createWriteStream({
//     metadata: {
//         contentType: req.file.mimetype
//     }
//   });

//   blobStream.on("error", (err) => {
//     next(err);
//   });

//   blobStream.on("finish", () => {
//     // The public URL can be used to directly access the file via HTTP.
//     const publicUrl = format(`https://storage.googleapis.com/${bucket.name}/${blob.name}`);
//     res.status(200).json({ publicUrl });
//   });

//   blobStream.end(req.file.buffer);
//   console.log(req.file);

// });

// var express = require('express');
// var path = require('path')
// var multer  = require('multer')
// var upload = multer().array('imgCollection')

// const cors = require('cors')

// const app = express()
// const port = 5000;

// app.use(cors())

// app.post('/api/interview/upload', function(req, res, next) {
//     // Imports the Google Cloud client library.
//     const {Storage} = require('@google-cloud/storage');
  
//     const storage = new Storage({projectId: 'cloud-api-test-365605', keyFilename: path.join(__dirname, './cred_key.json')});
  
//     try {
//       async function uploadFile(file, folder) {
//         let bucketName = 'data'
//         let bucket = storage.bucket(bucketName)
  
//         let newFileName = folder + '/' + file.originalname;
  
//         let fileUpload = bucket.file(newFileName);
//         const blobStream = fileUpload.createWriteStream({
//             metadata: {
//                 contentType: file.mimetype
//             }
//         });
  
//         blobStream.on('error', (error) => {
//             console.log('Something is wrong! Unable to upload at the moment.' + error);
//         });
  
//         blobStream.on('finish', () => {
//             const url = `https://storage.googleapis.com/${bucket.name}/${fileUpload.name}`; //image url from firebase server
//             console.log(url)
  
//         });
  
//         blobStream.end(file.buffer);
//       }
  
//       upload(req, res, function(err) {
//         let files = req.files
  
//         for (let file in files) {
//           uploadFile(files[file], `11/1`)
//         }
  
//         if(err) {
//             return res.send("Error uploading file." + err);
//         }
//         res.send("File is uploaded");
//       })
//     } catch (err) {
//       res.send(err)
//     }
//   });
  


// app.listen(port, () => {
//   console.log(`listening at http://localhost:${port}`);
// });

//Imports
const express = require('express');
const multer = require('multer');
const cors = require('cors')

// set up multer
var storage = multer.diskStorage({
    destination: function (req, file, cb) {
      cb(null, `uploadedFiles`)
    },
    filename: function (req, file, cb) {
      cb(null, `${file.originalname.split('.')[0]}_${req.query.id}_${req.query.qn}${file.originalname.split('.')[1]}`)
    }
})
//create multer instance
var upload = multer({ storage: storage })

// create app 
port = 5000;
const app = express();

var corsOptions = {
    origin: '*',
    optionsSuccessStatus: 200 // some legacy browsers (IE11, various SmartTVs) choke on 204
  }

  app.use(cors(corsOptions))

app.listen(port,()=>{
    console.log("Server started on port :"+port)
});


// to use this API the user need to upload a single file using field name "filetoupload" when sending the POST request 
//and must send a JSON with "description" filed
app.post('/uploadfile', upload.single('filetoupload'), function (req, res, next) {  
    console.log(req.body.description);  
    res.status(200).send({'message' : "file uploaded"});
  })