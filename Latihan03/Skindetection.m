clc; clear; close all; warning off all;

%membaca citra RGB
I = imread('01.imageoriginal.jpg');
figure, imshow(I)

%mengekstrak masing-masing komponen citra rgb
R = I (:,:,1);
G = I (:,:,2);
B = I (:,:,3);

%invers terhadap nilai mean masing2 komponen
mR = 1/(mean(mean(R)));
mG = 1/(mean(mean(G)));
mB = 1/(mean(mean(B)));

% mencari nilai inverse yang maksimal
maxRGB = max(max(mR, mG), mG);

% menghitung nilai faktor skala
mR = mR/maxRGB;
mG = mG/maxRGB;
mB = mB/maxRGB;

% melakukan penskalaan nilai piksel
out = uint8(zeros(size(I)));
out(:,:,1) = R*mR;
out(:,:,2) = G*mG;
out(:,:,3) = B*mB;

figure, imshow(out)

% mengkonversi citra rgb nebhadu citra ycbcr
img_ycbcr = rgb2ycbcr(out);
figure, imshow(img_ycbcr)

% mengekstrak komponen Cb dan Cr
Cb = img_ycbcr(:,:,2);
Cr = img_ycbcr(:,:,3);
figure, imshow(img_ycbcr)

% melakukan deteksi warna kulit
[r,c,v] = find(Cb>=77 & Cb<=127 & Cr>=133 & Cr<=173);

% rekontruksi nilai piksel hasil deteksi 
numind = size(r,1);
bin = false(size(I,1),size(I,2));
for i = 1:numind
    bin(r(i), c(i)) = 1;
end
figure, imshow(bin)

bin = imfill(bin,'holes');
figure, imshow(bin)


%menampilkan citra rgb hasil segmentasi
R(~bin) = 0;
G(~bin) = 0;
B(~bin) = 0;
RGB = cat(3,R,G,B);

figure, imshow(RGB)


