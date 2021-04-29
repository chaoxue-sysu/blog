# 图片基础知识

## 位图与矢量图
### 位图
**位图**，亦称为点阵图像或栅格图像，是由像素点组成的。放大后会失真，与分辨率有关。常见的位图格式有jpg,png等。常用的位图处理工具有Adobe Photoshop。

与矢量图不同，位图的大小由像素点的多少决定。位图一般有三个属性，像素大小（Pixels），尺寸（如Inch,英寸，1英寸=2.54厘米），PPI（Pixels Per Inch, 每英寸像素），他们之间的关系为，像素=尺寸(in)×PPI。可以看出，一张位图是否“清楚”（是否能够包含足够的信息，看的清楚），取决于整体像素点的大小，而不是PPI。当然同等大小下，PPI越大，像素点也就越多，就越清楚。需要注意的是，通过图形放大来增加图像像素大小，但并未增加图片的信息量，图片并未变清楚，是无效的变换。与PPI 类似的概念有DPI(Dots Per Inch)，是针对印刷设备而言的，如打印机，常用于纸质出版物中。

### 矢量图
**矢量图**，也称为面向对象的图像或绘图图像，在数学上定义为一系列由线连接的点。它的特点是放大后图像不会失真，和分辨率无关，适用于图形设计、文字设计和一些标志设计、版式设计等。矢量图的常见格式有ico,bw,svg,mwf/emf(微软windows适用),eps(用PostScript语言描述),ai(Adobe Illustrator)等。常用的矢量图处理工具有Adobe Illustrator。

### 出版图片要求
以Natrue杂志为例，其对出版图片的 [要求](https://www.nature.com/nature/for-authors/final-submission)：尽可能使用矢量图，不要将矢量图转为位图，位图的分辨率300-600 dpi。

>Layered Photoshop (PSD) or TIFF format (high resolution, 300–600 dots per inch (dpi) for photographic images. In Photoshop, it is possible to create images with separate components on different layers. This is particularly useful for placing text labels or arrows over an image, as it allows them to be edited later. If you have done this, please send the Photoshop file (.psd) with the layers intact.

>Adobe Illustrator (AI), Postscript, Vector EPS or PDF format for figures containing line drawings and graphs, including figures combining text and line art with photographs or scans.


**参考：**
* [为何分辨率满足要求，图片还是被杂志退回？](https://www.xiahepublishing.com/2475-7543/MRP-2016-061)




