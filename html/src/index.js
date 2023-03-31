// Set up.


function setupApp() {

    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Set up size input boxes.                                                                                      //
    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    const sizeLogNormalShape = $("#sizeLogNormalShape");
    const sizeLogNormalLocation = $("#sizeLogNormalLocation");
    const sizeLogNormalScale = $("#sizeLogNormalScale");

    sizeLogNormalShape.attr("value", "0.3");
    sizeLogNormalShape.on("keyup", sizeLogNormalShapeKeyUp);

    sizeLogNormalLocation.attr("value", "1.0");
    sizeLogNormalLocation.on("keyup", sizeLogNormalLocationKeyUp);

    sizeLogNormalScale.attr("value", "90.0");
    sizeLogNormalScale.on("keyup", sizeLogNormalScaleKeyUp);

    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Set up size input boxes.                                                                                      //
    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    const aspectRatioLogNormalShape = $("#aspectRatioLogNormalShape");
    const aspectRatioLogNormalLocation = $("#aspectRatioLogNormalLocation");
    const aspectRatioLogNormalScale = $("#aspectRatioLogNormalScale");

    aspectRatioLogNormalShape.attr("value", "0.9");
    aspectRatioLogNormalShape.on("keyup", aspectRatioLogNormalShapeKeyUp);

    aspectRatioLogNormalLocation.attr("value", "1.0");
    aspectRatioLogNormalLocation.on("keyup", aspectRatioLogNormalLocationKeyUp);

    aspectRatioLogNormalScale.attr("value", "0.8");
    aspectRatioLogNormalScale.on("keyup", aspectRatioLogNormalScaleKeyUp);

    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // Set up smoothing factor box.                                                                                  //
    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    const smoothingFactor = $("#smoothingFactor");

    smoothingFactor.attr("value", 3);
    smoothingFactor.on("keyup", smoothingFactorKeyUp);

}


function updateFigures() {

    const forcDiagram = $("#forcDiagram");
    const forcLoopsDiagram = $("#forcLoopsDiagram");

    forcDiagram.attr("src", "src/clear.png");
    forcLoopsDiagram.attr("src", "src/clear.png");

    // Download the FORC diagram.

    const downloadingForcImage = new Image();
    downloadingForcImage.onerror = forcDiagramNotFound;
    const forcDiagramUrl = logNormalForcDiagramUrlPng(
        $("#aspectRatioLogNormalShape").attr("value"),
        $("#aspectRatioLogNormalLocation").attr("value"),
        $("#aspectRatioLogNormalScale").attr("value"),
        $("#sizeLogNormalShape").attr("value"),
        $("#sizeLogNormalLocation").attr("value"),
        $("#sizeLogNormalScale").attr("value"),
        $("#smoothingFactor").attr("value"));
    console.log(forcDiagramUrl);

    downloadingForcImage.onload = function () {
        forcDiagram.attr("src", downloadingForcImage.src);
    };

    downloadingForcImage.src = forcDiagramUrl;

    // Download the FORC loops diagram.

    const downloadingForcLoopsImage = new Image();
    downloadingForcLoopsImage.onerror = forcLoopsDiagramNotFound;
    const forcDiagramLoopsUrl = logNormalForcLoopsDiagramUrlPng(
        $("#aspectRatioLogNormalShape").attr("value"),
        $("#aspectRatioLogNormalLocation").attr("value"),
        $("#aspectRatioLogNormalScale").attr("value"),
        $("#sizeLogNormalShape").attr("value"),
        $("#sizeLogNormalLocation").attr("value"),
        $("#sizeLogNormalScale").attr("value"),
        $("#smoothingFactor").attr("value"));
    console.log(forcDiagramLoopsUrl);

    downloadingForcLoopsImage.onload = function () {
        forcLoopsDiagram.attr("src", downloadingForcLoopsImage.src);
    };

    downloadingForcLoopsImage.src = forcDiagramLoopsUrl;

}


function forcDiagramNotFound() {
    const forcDiagram = $("#forcDiagram");
    forcDiagram.attr("src", "src/notFound.png");
}


function forcLoopsDiagramNotFound() {
    const forcLoopsDiagram = $("#forcLoopsDiagram");
    forcLoopsDiagram.attr("src", "src/notFound.png");
}


function logNormalForcDiagramUrlPng(aspectRatioShape,
                                    aspectRatioLocation,
                                    aspectRatioScale,
                                    sizeShape,
                                    sizeLocation,
                                    sizeScale,
                                    smoothingFactor) {

    return `http://185.125.169.90:8888/lognormal-forc-png?aspect_ratio_shape=${aspectRatioShape}&aspect_ratio_location=${aspectRatioLocation}&aspect_ratio_scale=${aspectRatioScale}&size_shape=${sizeShape}&size_location=${sizeLocation}&size_scale=${sizeScale}&smoothing_factor=${smoothingFactor}`;

}


function logNormalForcLoopsDiagramUrlPng(aspectRatioShape,
                                         aspectRatioLocation,
                                         aspectRatioScale,
                                         sizeShape,
                                         sizeLocation,
                                         sizeScale,
                                         smoothingFactor) {

    return `http://185.125.169.90:8888/lognormal-forc-loops-png?aspect_ratio_shape=${aspectRatioShape}&aspect_ratio_location=${aspectRatioLocation}&aspect_ratio_scale=${aspectRatioScale}&size_shape=${sizeShape}&size_location=${sizeLocation}&size_scale=${sizeScale}&smoothing_factor=${smoothingFactor}`;

}

// GUI elements.

function updateClicked() {
    updateFigures();
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Keyup / typing events for size text boxes.                                                                        //
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function sizeLogNormalShapeKeyUp(event) {
    console.log("sizeLogNormalShapeKeyUp(): event: ", this.value);
    const sizeLogNormalShape = $("#sizeLogNormalShape");
    sizeLogNormalShape.attr("value", this.value);
    updateSizeLogNormalDistribution();
}


function sizeLogNormalLocationKeyUp(event) {
    console.log("sizeLogNormalLocationKeyUp(): event: ", this.value);
    const sizeLogNormalLocation = $("#sizeLogNormalLocation");
    sizeLogNormalLocation.attr("value", this.value);
    updateSizeLogNormalDistribution();
}


function sizeLogNormalScaleKeyUp(event) {
    console.log("sizeLogNormalScaleKeyUp(): event: ", this.value);
    const sizeLogNormalScale = $("#sizeLogNormalScale");
    sizeLogNormalScale.attr("value", this.value);
    updateSizeLogNormalDistribution();
}


///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Keyup / typing events for aspect ratio text boxes.                                                                //
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function aspectRatioLogNormalShapeKeyUp(event) {
    const aspectRatioLogNormalShape = $("#aspectRatioLogNormalShape");
    aspectRatioLogNormalShape.attr("value", this.value);
    updateAspectRatioLogNormalDistribution();
}

function aspectRatioLogNormalLocationKeyUp(event) {
    const aspectRatioLogNormalLocation = $("#aspectRatioLogNormalLocation");
    aspectRatioLogNormalLocation.attr("value", this.value);
    updateAspectRatioLogNormalDistribution();
}


function aspectRatioLogNormalScaleKeyUp(event) {
    const aspectRatioLogNormalScale = $("#aspectRatioLogNormalScale");
    aspectRatioLogNormalScale.attr("value", this.value);
    updateAspectRatioLogNormalDistribution();
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Keyup / typing events for aspect ratio text boxes.                                                                //
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function smoothingFactorKeyUp(event) {
    const smoothingFactor = $("#smoothingFactor");
    smoothingFactor.attr("value", this.value);
}

// Functions

function logNormalFunc(shape, location, scale) {
    return function (x) {
        return 1/(Math.exp(Math.pow(Math.log((-location + x)/scale),2)/(2.*Math.pow(shape,2)))*Math.sqrt(2*Math.PI)*shape*(-location + x));
    };
}


function makeArr(startValue, stopValue, cardinality) {
    const arr = [];
    const step = (stopValue - startValue) / (cardinality - 1);
    for (let i = 0; i < cardinality; i++) {
        arr.push(startValue + (step * i));
    }
    return arr;
}


function getStandardDeviation (array) {
    const n = array.length
    const mean = array.reduce((a, b) => a + b) / n
    return Math.sqrt(array.map(x => Math.pow(x - mean, 2)).reduce((a, b) => a + b) / n)
}
